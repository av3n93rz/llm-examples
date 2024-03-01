import { z } from 'zod';

export const sendMessageResponseParser = z.object({
  message: z.string(),
});
