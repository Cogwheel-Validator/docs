import { createOpenAPI } from "fumadocs-openapi/server";

// Two separate servers (rather than one server with two schema entries) so
// each version's generated pages live under their own output directory and
// can be regenerated/reasoned about independently. Server-safe (used from
// page.tsx to preload a page's schema before render) - the interactive
// OpenAPIPage component itself lives in ./openapi-page.tsx since it's
// client-only.
export const openapiV1 = createOpenAPI({
  input: ["./openapi-specs/pathfinder-v1.yaml"],
});

export const openapiV2beta = createOpenAPI({
  input: ["./openapi-specs/pathfinder-v2beta.yaml"],
});
