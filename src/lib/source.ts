import { networks, services, spectraPortal } from "@/.source";
import { loader } from "fumadocs-core/source";
import { toFumadocsSource } from "fumadocs-mdx/runtime/server";

// See https://fumadocs.vercel.app/docs/headless/source-api for more info
// Networks documentation source
export const networksSource = loader({
  baseUrl: "/networks",
  source: toFumadocsSource(networks, []),
});

// Services documentation source
export const servicesSource = loader({
  baseUrl: "/services",
  source: toFumadocsSource(services, []),
});

// Spectra Portal documentation source
export const spectraPortalSource = loader({
  baseUrl: "/spectra-portal",
  source: toFumadocsSource(spectraPortal, []),
});