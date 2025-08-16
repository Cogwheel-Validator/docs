import { networksSource, servicesSource } from "@/lib/source";
import { createFromSource, createSearchAPI } from "fumadocs-core/search/server";

export const { GET } = createSearchAPI('advanced', {
  indexes: [
    ...networksSource.getPages().map((page) => ({
      title: page.data.title,
      description: page.data.description,
      url: page.url,
      id: page.url,
      structuredData: page.data.structuredData,
    })),
    ...servicesSource.getPages().map((page) => ({
      title: page.data.title,
      description: page.data.description,
      url: page.url,
      id: page.url,
      structuredData: page.data.structuredData,
    })),
  ],
  language: 'english',
});