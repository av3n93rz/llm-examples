import type {
  APIConversationResponseMessage,
  APISendMessagePayload,
  ConversationResponseMessage,
  SendMessagePayload,
} from './types';

export class ConversationMapper {
  static fromDomain(payload: SendMessagePayload): APISendMessagePayload {
    return {
      user_id: payload.userId,
      conversation_id: payload.conversationId,
      message: payload.message,
    };
  }

  static toDomain(
    response: APIConversationResponseMessage,
  ): ConversationResponseMessage {
    return {
      message: response.message,
    };
  }
}
