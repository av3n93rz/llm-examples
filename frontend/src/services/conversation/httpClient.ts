import axios from 'axios';
import ms from 'ms';

import { ConversationMapper } from './conversation.mapper';
import { sendMessageResponseParser } from './httpClient.schema';
import type { SendMessage } from './types';

export class ConversationClient {
  static sendMessage: SendMessage = async payload => {
    const requestBody = ConversationMapper.fromDomain(payload);
    const res = await axios.post('/api/conversation', requestBody, {
      timeout: ms('5m'),
    });
    const data = sendMessageResponseParser.parse(res.data);
    return ConversationMapper.toDomain(data);
  };
}
