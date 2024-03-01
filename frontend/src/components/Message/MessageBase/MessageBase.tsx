import { cva } from 'class-variance-authority';
import type { FC, PropsWithChildren } from 'react';

import { cn } from '@/lib/utils';

import { MessageTail } from '../MessageTail';

const messageBaseVariants = cva('flex w-full p-4', {
  variants: {
    direction: {
      left: 'justify-start',
      right: 'justify-end',
    },
  },
  defaultVariants: {
    direction: 'left',
  },
});

const messageContainerVariants = cva(
  'p-4 font-mono text-sm text-white backdrop-blur',
  {
    variants: {
      direction: {
        left: '',
        right: 'bg-foreground',
      },
    },
    defaultVariants: {
      direction: 'left',
    },
  },
);

type MessageBaseProps = {
  direction?: 'left' | 'right';
  backgroundColor?: string;
};

export const MessageBase: FC<PropsWithChildren<MessageBaseProps>> = ({
  direction,
  children,
  backgroundColor,
}) => (
  <div className={cn(messageBaseVariants({ direction }))}>
    <div className="relative max-w-[90%] border border-border">
      <div
        className={cn(
          messageContainerVariants({ direction, className: backgroundColor }),
        )}>
        {children}
        <MessageTail direction={direction} backgroundColor={backgroundColor} />
      </div>
    </div>
  </div>
);
