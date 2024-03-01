import type { ErrorMessage as ErrorMessageType } from '@/types/message';

import { MessageBase } from '..';

type ErrorMessageProps = {
  message: ErrorMessageType;
};

export const ErrorMessage = ({ message }: ErrorMessageProps) => (
  <MessageBase backgroundColor="bg-red-800">{message.message}</MessageBase>
);
