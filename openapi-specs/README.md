# OpenAPI specs

`pathfinder-v1.yaml` and `pathfinder-v2beta.yaml` are copies of the OpenAPI 3.1 specs generated in the [`spectra-ibc-hub`](https://github.com/Cogwheel-Validator/spectra-portal) repo (`docs/openapi/{v1,v2beta}.openapi.yaml`, generated there via `make generate-openapi`).

They're pulled in with `pnpm run sync:pathfinder` (see `scripts/sync-pathfinder-docs.mjs`), run manually by a maintainer - there's no automated/live sync. After running it, review the `git diff` here before committing.

Don't hand-edit these files; the diff would just get overwritten on the next sync.

After syncing new specs, regenerate the API reference pages with `pnpm run generate:api`.
