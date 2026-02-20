import { z, defineCollection } from "astro:content";

const gear = defineCollection({
  type: "content",
  schema: z.object({
    title: z.string(),
    // slug is derived from the filename; not required in frontmatter
    description: z.string(),
    url: z.string().optional(),
    tags: z.array(z.string()),
  }),
});

export const collections = { gear };
