import {
  defineConfig,
  defineDocs,
  defineCollections,
  frontmatterSchema,
  metaSchema,
} from "fumadocs-mdx/config";

// You can customise Zod schemas for frontmatter and `meta.json` here
// see https://fumadocs.vercel.app/docs/mdx/collections#define-docs
export const docs = defineDocs({
  docs: {
    schema: frontmatterSchema,
  },
  meta: {
    schema: metaSchema,
  },
});

// Define networks documentation collection
export const networks = defineCollections({
  type: 'doc',
  dir: 'content/networks',
  schema: frontmatterSchema,
});

// Define services documentation collection
export const services = defineCollections({
  type: 'doc',
  dir: 'content/services',
  schema: frontmatterSchema,
});

// Combined collection for search that includes both networks and services
export const combined = defineCollections({
  type: 'doc',
  dir: ['content/networks', 'content/services'],
  schema: frontmatterSchema,
});

export default defineConfig({
  mdxOptions: {
    // MDX options
  },
});
