import { cva } from 'class-variance-authority';

import { cn } from '@/lib/utils';

const tailContainerVariants = cva(
  'absolute -bottom-3 w-6 overflow-hidden border-border',
  {
    variants: {
      direction: {
        left: '-left-px border-l',
        right: '-right-px border-r',
      },
    },
    defaultVariants: {
      direction: 'left',
    },
  },
);

const tailVariants = cva('h-3 w-6 transform border border-border', {
  variants: {
    direction: {
      left: 'origin-bottom-left -rotate-45 bg-black/[0.96]',
      right: 'origin-bottom-right -translate-x-px rotate-45 bg-foreground',
    },
  },
  defaultVariants: {
    direction: 'left',
  },
});

type MessageTailProps = {
  direction?: 'left' | 'right';
  backgroundColor?: string;
};

export const MessageTail = ({
  direction,
  backgroundColor,
}: MessageTailProps) => (
  <div className={cn(tailContainerVariants({ direction }))}>
    <div className={cn(tailVariants({ direction }), backgroundColor)} />
  </div>
);
