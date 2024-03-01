import { atom } from 'jotai';

import type { Message } from '@/types/message';

export const isThinkingAtom = atom(false);
export const isTypingAtom = atom(false);
export const isWorkingAtom = atom(
  get => get(isThinkingAtom) || get(isTypingAtom),
);
export const conversationHistoryAtom = atom<Message[]>([]);
