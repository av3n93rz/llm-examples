'use client';

import { UserProvider } from '@auth0/nextjs-auth0/client';
import { Provider } from 'jotai';
import { type PropsWithChildren } from 'react';

export default function Template({ children }: PropsWithChildren) {
  return (
    <UserProvider>
      <Provider>{children}</Provider>
    </UserProvider>
  );
}
