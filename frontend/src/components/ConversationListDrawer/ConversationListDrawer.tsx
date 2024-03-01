import { AlignJustify } from 'lucide-react';

import { Button } from '@/components/ui/button';
import { Drawer, DrawerContent, DrawerTrigger } from '@/components/ui/drawer';

import { ConversationList } from '../ConversationList';

export const ConversationListDrawer = () => (
  <Drawer direction="left">
    <DrawerTrigger asChild>
      <Button
        variant="ghost"
        size="icon"
        className="text-white hover:text-black">
        <AlignJustify />
      </Button>
    </DrawerTrigger>
    <DrawerContent
      className="w-fit border-none bg-transparent"
      overlayProps={{ className: 'bg-black/[0.3]' }}>
      <div className="flex min-h-screen flex-col rounded-xl p-6">
        <ConversationList className="min-h-0 flex-grow bg-black/[0.96]" />
      </div>
    </DrawerContent>
  </Drawer>
);
