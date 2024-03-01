import { ConversationHistory } from '../ConversationHistory';
import { ConversationInputForm } from '../ConversationInputForm';

export const ConversationWindow = () => (
  <div className="flex max-h-screen min-h-screen flex-1 flex-col items-center px-4 py-24 md:pl-0 lg:pl-0 lg:pr-24">
    <div className="flex w-full max-w-[1024px] flex-grow flex-col overflow-hidden rounded-xl border border-border bg-transparent">
      <ConversationHistory />
      <ConversationInputForm />
    </div>
  </div>
);
