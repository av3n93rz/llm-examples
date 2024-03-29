module.exports = {
  plugins: [
    require.resolve("@trivago/prettier-plugin-sort-imports"),
    require.resolve("prettier-plugin-tailwindcss"),
  ],
  htmlWhitespaceSensitivity: "css",
  singleQuote: true,
  tabWidth: 2,
  trailingComma: "all",
  useTabs: false,
  importOrder: ["^@/(.*)$", "^[./]"],
  importOrderSeparation: true,
  importOrderSortSpecifiers: true,
  arrowParens: "avoid",
  bracketSameLine: true,
  bracketSpacing: true,
};
