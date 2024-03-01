import Lottie from 'lottie-react';

import { MessageBase } from '..';
import animationData from './animation-data.json';

export const LoadingMessage = () => (
  <MessageBase>
    <div className="h-[24px] w-[24px]">
      <Lottie animationData={animationData} loop />
    </div>
  </MessageBase>
);
