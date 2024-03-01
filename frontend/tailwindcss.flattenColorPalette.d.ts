/* eslint-disable */
declare module 'tailwindcss/lib/util/flattenColorPalette' {
  import type { Config } from 'tailwindcss';

  interface RecursiveKeyValuePair<K extends keyof any = string, V = string> {
    [key: string]: V | RecursiveKeyValuePair<K, V>;
  }

  function flattenColorPalette(colors: Config['theme']): Record<string, string>;
  export default flattenColorPalette;
}
