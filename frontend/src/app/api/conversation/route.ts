import { getAccessToken } from '@auth0/nextjs-auth0';
import ms from 'ms';
import type { NextRequest } from 'next/server';
import { NextResponse } from 'next/server';
import { z } from 'zod';

import { apiClient } from '../api_client';

const bodyParser = z.object({
  user_id: z.string(),
  conversation_id: z.string(),
  message: z.string(),
});

export async function POST(request: NextRequest) {
  const { accessToken } = await getAccessToken();

  if (!accessToken) {
    return new Response('Unauthorized', {
      status: 401,
    });
  }

  const requestBody = await request.json();
  const body = bodyParser.parse(requestBody);
  const { data } = await apiClient.post('/conversation', body, {
    timeout: ms('5m'), // Chatbots can be slow to respond
  });
  return NextResponse.json(data);
}
