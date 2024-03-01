import type { Message } from '@/types/message';

import { BotMessage } from '../BotMessage';
import { ErrorMessage } from '../ErrorMessage';
import { LoadingMessage } from '../LoadingMessage';
import { UserMessage } from '../UserMessage';

type Props = {
  message: Message;
};

export const MessageMapper = ({ message }: Props) => {
  switch (message.type) {
    case 'userMessage':
      return <UserMessage message={message} />;
    case 'loadingMessage':
      return <LoadingMessage />;
    case 'errorMessage':
      return <ErrorMessage message={message} />;
    case 'botMessage':
      return <BotMessage message={message} />;
  }
};
