// Regenerates the interactive Pathfinder API reference pages from the
// synced OpenAPI specs under openapi-specs/. Run after `pnpm run sync:pathfinder`
// whenever the specs change, or any time you want to pick up a manual edit.
//
// Usage: pnpm run generate:api

import { generateFiles } from "fumadocs-openapi";
import { openapiV1, openapiV2beta } from "../src/lib/openapi.ts";

async function main() {
  await generateFiles({
    input: openapiV1,
    output: "./content/spectra-portal/api/v1",
    meta: true,
    per: "operation",
    groupBy: "tag",
  });

  await generateFiles({
    input: openapiV2beta,
    output: "./content/spectra-portal/api/v2beta",
    meta: true,
    per: "operation",
    groupBy: "tag",
    // FindPathStreaming is a bidirectional-streaming RPC - it has no
    // request/response shape a "try it" form UI can represent, and Scalar's
    // playground can't drive a stream. Its full contract is documented in
    // pathfinder-v2beta.mdx instead; drop the (broken) generated page for it
    // and its dangling meta.json reference.
    beforeWrite(files) {
      for (let i = files.length - 1; i >= 0; i--) {
        if (files[i].path.includes("FindPathStreaming")) files.splice(i, 1);
      }
      for (const file of files) {
        if (file.path.endsWith("meta.json") && file.content.includes("FindPathStreaming")) {
          const meta = JSON.parse(file.content);
          if (Array.isArray(meta.pages)) {
            meta.pages = meta.pages.filter(
              (p: string) => !p.includes("FindPathStreaming"),
            );
          }
          file.content = JSON.stringify(meta, null, 2);
        }
      }
    },
  });

  console.log("Generated Pathfinder API reference pages.");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
