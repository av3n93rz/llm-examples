'use client';

import { useAtomValue } from 'jotai';
import type { KeyboardEventHandler } from 'react';
import { createRef, useCallback, useEffect } from 'react';

import { isWorkingAtom } from '@/atoms/atoms';
import { useSendMessage } from '@/hooks/useSendMessage';

export const ConversationInputForm = () => {
  const textareaRef = createRef<HTMLTextAreaElement>();
  const isWorking = useAtomValue(isWorkingAtom);
  const sendMessage = useSendMessage();

  // Resize the textarea as the user types
  useEffect(() => {
    const textarea = textareaRef.current;
    if (!textarea) {
      return;
    }
    textarea.style.height = 'auto'; // Reset height first to get accurate scrollHeight
    textarea.style.height = `${textarea.scrollHeight}px`;
  }, [textareaRef.current?.value, textareaRef]);

  const handleKeyDown: KeyboardEventHandler<HTMLTextAreaElement> = useCallback(
    event => {
      if (event.key === 'Enter' && !event.shiftKey) {
        const message = event.currentTarget.value.trim();
        if (message.length === 0 || isWorking) {
          return;
        }
        event.preventDefault();
        sendMessage(message);
        event.currentTarget.value = '';
      }
    },
    [isWorking, sendMessage],
  );

  return (
    <form>
      <textarea
        className="max-h-[200px] w-full resize-none overflow-y-scroll border-t bg-transparent p-4 text-white scrollbar-thin scrollbar-track-transparent scrollbar-thumb-border focus:outline-none"
        ref={textareaRef}
        rows={1}
        placeholder="Aa"
        onKeyDown={handleKeyDown}
      />
    </form>
  );
};
