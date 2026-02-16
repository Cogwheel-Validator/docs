import { DocsLayout } from "fumadocs-ui/layouts/docs";
import type { ReactNode } from "react";
import { baseOptions } from "@/app/layout.config";
import { spectraPortalSource } from "@/lib/source";

export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout tree={spectraPortalSource.pageTree} {...baseOptions}>
      {children}
    </DocsLayout>
  );
} 