import { spectraPortalSource } from "@/lib/source";
import {
  DocsPage,
  DocsBody,
  DocsDescription,
  DocsTitle,
} from "fumadocs-ui/page";
import { notFound } from "next/navigation";
import { createRelativeLink } from "fumadocs-ui/mdx";
import { getMDXComponents } from "@/mdx-components";
import { openapiV1, openapiV2beta } from "@/lib/openapi";
import { OpenAPIPage } from "@/lib/openapi-page";

export default async function Page(props: {
  params: Promise<{ slug?: string[] }>;
}) {
  const params = await props.params;
  const page = spectraPortalSource.getPage(params.slug);
  if (!page) notFound();

  const MDXContent = page.data.body;

  // Pages generated under api/v1 or api/v2beta need their OpenAPI schema
  // preloaded server-side, then bound onto the OpenAPIPage component the
  // generated MDX references - the generated Layout only passes
  // `document`/`operations` to it, not the page's own props, so `preloaded`
  // has to be baked into the component reference itself.
  const openapiServer =
    params.slug?.[0] === "api"
      ? params.slug?.[1] === "v2beta"
        ? openapiV2beta
        : openapiV1
      : undefined;
  const openapiProps = openapiServer
    ? await openapiServer.preloadOpenAPIPage(page)
    : undefined;

  return (
    <DocsPage toc={page.data.toc} full={page.data.full}>
      <DocsTitle>{page.data.title}</DocsTitle>
      <DocsDescription>{page.data.description}</DocsDescription>
      <DocsBody>
        <MDXContent
          components={getMDXComponents({
            // this allows you to link to other pages with relative file paths
            a: createRelativeLink(spectraPortalSource, page),
            ...(openapiProps
              ? {
                  OpenAPIPage: (mdxProps: Record<string, unknown>) => (
                    <OpenAPIPage
                      // eslint-disable-next-line @typescript-eslint/no-explicit-any
                      {...({ ...mdxProps, ...openapiProps } as any)}
                    />
                  ),
                }
              : {}),
          })}
        />
      </DocsBody>
    </DocsPage>
  );
}

export async function generateStaticParams() {
  return spectraPortalSource.generateParams();
}

export async function generateMetadata(props: {
  params: Promise<{ slug?: string[] }>;
}) {
  const params = await props.params;
  const page = spectraPortalSource.getPage(params.slug);
  if (!page) notFound();

  return {
    title: page.data.title,
    description: page.data.description,
  };
} 