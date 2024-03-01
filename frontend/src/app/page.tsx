import { Header } from '@/components/Header';
import { Spotlight } from '@/components/ui/Spotlight';
import { Chat } from '@/features/chat';

export default function Home() {
  return (
    <main className="flex bg-black/[0.96] antialiased bg-grid-white/[0.02] md:gap-4">
      <Spotlight
        className="-top-40 left-0 md:-top-20 md:left-60"
        fill="white"
      />
      <Header />
      <Chat />
    </main>
  );
}
