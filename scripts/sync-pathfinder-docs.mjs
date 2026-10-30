// Manually-run script that pulls the generated Pathfinder OpenAPI specs from
// the spectra-ibc-hub repo. Not wired into CI or any build step on purpose -
// run it, review the git diff, commit if it looks right.
//
// Usage:
//   node scripts/sync-pathfinder-docs.mjs [--ref=<branch-or-tag>]
//   pnpm run sync:pathfinder -- --ref=dev   (to test against unreleased content)

import { writeFile } from "node:fs/promises";
import path from "node:path";

const REPO_OWNER = "Cogwheel-Validator";
const REPO_NAME = "spectra-portal";
const DEFAULT_REF = "main";

const refArg = process.argv.find((arg) => arg.startsWith("--ref="));
const ref = refArg ? refArg.slice("--ref=".length) : DEFAULT_REF;

const FILES = [
  {
    source: "docs/openapi/v1.openapi.yaml",
    dest: "openapi-specs/pathfinder-v1.yaml",
  },
  {
    source: "docs/openapi/v2beta.openapi.yaml",
    dest: "openapi-specs/pathfinder-v2beta.yaml",
  },
];

async function syncFile({ source, dest }) {
  const url = `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${ref}/${source}`;
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(
      `Failed to fetch ${url}: ${response.status} ${response.statusText}`,
    );
  }
  const text = await response.text();
  const destPath = path.join(process.cwd(), dest);
  await writeFile(destPath, text);
  return { dest, bytes: text.length };
}

async function main() {
  console.log(`Syncing Pathfinder OpenAPI specs from ${REPO_OWNER}/${REPO_NAME}@${ref}...`);
  const results = [];
  for (const file of FILES) {
    results.push(await syncFile(file));
  }
  for (const { dest, bytes } of results) {
    console.log(`  wrote ${dest} (${bytes} bytes)`);
  }
  console.log(
    `Synced ${results.length} file(s). Review the git diff, then run 'pnpm run generate:api' to rebuild the reference pages.`,
  );
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
