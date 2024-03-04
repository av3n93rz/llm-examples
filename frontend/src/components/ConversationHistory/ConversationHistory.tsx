'use client';

import { useAtomValue } from 'jotai';
import { createRef, useEffect } from 'react';

import { conversationHistoryAtom } from '@/atoms/atoms';

import { MessageMapper } from '../Message/MessageMapper';
import { ScrollFade } from '../ScrollFade';

const scrollToLastChatMessage = (element: HTMLDivElement | null) => {
  const parent = element?.parentElement;
  if (parent?.scrollHeight && parent.scrollHeight > parent.clientHeight) {
    element?.scrollIntoView({ behavior: 'smooth' });
  }
};

export const ConversationHistory = () => {
  const conversationHistory = useAtomValue(conversationHistoryAtom);
  const endOfConversationRef = createRef<HTMLDivElement>();

  useEffect(() => {
    setTimeout(
      () => scrollToLastChatMessage(endOfConversationRef.current),
      250,
    );
  }, [endOfConversationRef]);

  return (
    <div className="flex-grow overflow-auto scrollbar-thin scrollbar-track-transparent scrollbar-thumb-border">
      {conversationHistory.map(message => (
        <MessageMapper message={message} key={message.id} />
      ))}
      <div ref={endOfConversationRef} className="h-6 w-full bg-red-600 pt-10" />
      <ScrollFade />
    </div>
  );
};
