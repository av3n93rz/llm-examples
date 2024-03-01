import { ConversationListDrawer } from '../ConversationListDrawer';

export const Header = () => (
  <div className="absolute left-0 top-0 ml-4 mt-8 flex gap-4 lg:ml-24">
    <div className="md:hidden">
      <ConversationListDrawer />
    </div>
    <h1 className="text-2xl text-white">Logo</h1>
  </div>
);
