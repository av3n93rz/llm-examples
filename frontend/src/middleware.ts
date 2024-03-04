import { withMiddlewareAuthRequired } from '@auth0/nextjs-auth0/edge';

export default withMiddlewareAuthRequired();

export const config = {
  matcher: [
    /*
     * Match all request paths except for:
     * - api/health
     * - api/auth/*
     */
    '/((?!api/health|api/auth).*)',
  ],
};
