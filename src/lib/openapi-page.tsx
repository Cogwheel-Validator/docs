"use client";

import { createOpenAPIPage } from "fumadocs-openapi/ui";
import { withScalar } from "fumadocs-openapi/scalar";

// Shared interactive "try it" component (Scalar-powered), registered in
// mdx-components.tsx and consumed by the pages generated under
// content/spectra-portal/api/. withScalar() is client-only, so this must
// stay in its own "use client" module, separate from openapi.ts's
// server-safe createOpenAPI() instances.
export const OpenAPIPage = createOpenAPIPage(
  withScalar({
    // The Pathfinder specs also declare an application/proto content type
    // (Connect's binary wire format). There's no meaningful hand-editable
    // JSON form for it, so treat it like JSON for the playground/example
    // code rather than crashing - it's still the same underlying message
    // schema, just a different wire encoding on the real server.
    mediaAdapters: {
      "application/proto": {
        encode(data) {
          return JSON.stringify(data.body);
        },
        generateExample(data) {
          return `// application/proto is Connect's binary wire format - see the
// application/json example for the equivalent message shape.
const body = ${JSON.stringify(data.body, null, 2)};`;
        },
      },
    },
  }),
);
