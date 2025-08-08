import { docs, networks, services } from "@/.source";
import { loader } from "fumadocs-core/source";
import { createMDXSource } from "fumadocs-mdx";

// See https://fumadocs.vercel.app/docs/headless/source-api for more info
export const source = loader({
  // it assigns a URL to your pages
  baseUrl: "/docs",
  source: docs.toFumadocsSource(),
});

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
