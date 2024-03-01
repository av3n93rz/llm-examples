import { ConversationList } from '@/components/ConversationList';
import { ConversationWindow } from '@/components/ConversationWindow';

export const Chat = () => (
  <>
    <div className="hidden md:block">
      <ConversationList className="py-24 pl-4 lg:pl-24" />
    </div>
    <ConversationWindow />
  </>
);
