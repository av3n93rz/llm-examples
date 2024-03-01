import { useAtom, useSetAtom } from 'jotai';
import { useCallback } from 'react';
import { v4 } from 'uuid';

import { conversationHistoryAtom, isThinkingAtom } from '@/atoms/atoms';
import { ConversationClient } from '@/services/conversation';
import { Author } from '@/types/author';

const conversationId = 'conversation';
const userId = 'user';

export const useSendMessage = () => {
  const setIsThinking = useSetAtom(isThinkingAtom);
  const [conversationHistory, setConversationHistory] = useAtom(
    conversationHistoryAtom,
  );

  const sendMessage = useCallback(
    async (message: string) => {
      setIsThinking(true);

      setConversationHistory([
        ...conversationHistory,
        {
          id: v4(),
          type: 'userMessage',
          author: Author.USER,
          message,
        },
        {
          id: v4(),
          type: 'loadingMessage',
          author: Author.SYSTEM,
        },
      ]);

      try {
        const response = await ConversationClient.sendMessage({
          userId,
          conversationId,
          message,
        });

        setConversationHistory(prev => [
          // Remove the thinking message and add the answer
          ...prev.slice(0, -1),
          {
            id: v4(),
            type: 'botMessage',
            author: Author.BOT,
            message: response.message,
          },
        ]);
      } catch (error) {
        const errorMessage =
          'Oops, I could not answer that...' + '\n' + '```' + error + '```';
        setConversationHistory(prev => [
          // Remove the thinking message and add the answer
          ...prev.slice(0, -1),
          {
            id: v4(),
            type: 'errorMessage',
            author: Author.SYSTEM,
            message: errorMessage,
          },
        ]);
      } finally {
        setIsThinking(false);
      }
    },
    [setIsThinking, conversationHistory, setConversationHistory],
  );

  return sendMessage;
};
