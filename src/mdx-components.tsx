import defaultMdxComponents from "fumadocs-ui/mdx";
import type { MDXComponents } from "mdx/types";
import Callout from "@/components/Callout";
import NetworkGrid from "./components/NetworkGrid";
import Image from "next/image";
import Link from "next/link";
import { Mermaid } from "@/components/mermaid";

// use this function to get MDX components, you will need it for rendering MDX
export function getMDXComponents(components?: MDXComponents): MDXComponents {
  return {
    ...defaultMdxComponents,
    Callout,
    NetworkGrid,
    Image,
    Link,
    Mermaid,
    ...components,
  };
}
