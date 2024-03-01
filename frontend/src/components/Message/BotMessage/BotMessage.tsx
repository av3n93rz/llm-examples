import type { BotMessage as BotMessageType } from '@/types/message';

import { MessageBase } from '..';

type BotMessageProps = {
  message: BotMessageType;
};

export const BotMessage = ({ message }: BotMessageProps) => (
  <MessageBase>{message.message}</MessageBase>
);
