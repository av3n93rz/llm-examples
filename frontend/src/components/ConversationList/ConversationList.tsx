import { cn } from '@/lib/utils';

import { Button } from '../ui/button';

type ConversationListProps = {
  className?: string;
};

export const ConversationList = ({ className }: ConversationListProps) => (
  <div
    className={cn(
      'flex max-h-screen min-h-screen w-96 flex-col overflow-auto rounded-xl md:w-60 lg:w-96',
      className,
    )}>
    <div className="flex w-full flex-grow flex-col rounded-xl border border-border bg-transparent p-4">
      <h3 className="font-heading text-xl font-semibold tracking-tight text-neutral-200">
        Conversations
      </h3>
      <div className="flex flex-grow flex-col text-white">list of convos</div>
      <Button>Start new conversation</Button>
    </div>
  </div>
);
