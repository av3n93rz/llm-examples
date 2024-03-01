import type { Author } from './author';

export type UserMessage = {
  id: string;
  author: Author.USER;
  type: 'userMessage';
  message: string;
};

export type BotMessage = {
  id: string;
  author: Author.BOT;
  type: 'botMessage';
  message: string;
};

export type LoadingMessage = {
  id: string;
  author: Author.SYSTEM;
  type: 'loadingMessage';
};

export type ErrorMessage = {
  id: string;
  author: Author.SYSTEM;
  type: 'errorMessage';
  message: string;
};

export type Message = UserMessage | LoadingMessage | ErrorMessage | BotMessage;
