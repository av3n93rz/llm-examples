export type APISendMessagePayload = {
  user_id: string;
  conversation_id: string;
  message: string;
};

export type SendMessagePayload = {
  userId: string;
  conversationId: string;
  message: string;
};

export type APIConversationResponseMessage = {
  message: string;
};

export type ConversationResponseMessage = {
  message: string;
};

export type SendMessage = (
  payload: SendMessagePayload,
) => Promise<ConversationResponseMessage>;
