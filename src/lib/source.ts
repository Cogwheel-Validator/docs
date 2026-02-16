import { networks, services, spectraPortal } from "@/.source";
import { loader } from "fumadocs-core/source";
import { createMDXSource } from "fumadocs-mdx";

// See https://fumadocs.vercel.app/docs/headless/source-api for more info
// Networks documentation source
export const networksSource = loader({
  baseUrl: "/networks",
  source: createMDXSource(networks),
});

// Services documentation source
export const servicesSource = loader({
  baseUrl: "/services",
  source: createMDXSource(services),
});

// Spectra Portal documentation source
export const spectraPortalSource = loader({
  baseUrl: "/spectra-portal",
  source: createMDXSource(spectraPortal),
});