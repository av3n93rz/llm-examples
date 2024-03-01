import type { UserMessage as UserMessageType } from '@/types/message';

import { MessageBase } from '..';

type UserMessageProps = {
  message: UserMessageType;
};

export const UserMessage = ({ message }: UserMessageProps) => (
  <MessageBase direction="right">{message.message}</MessageBase>
);
