const html = require("eslint-plugin-html");
module.exports = [
  {
    plugins: { html },
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
      globals: { document: "readonly", window: "readonly", console: "readonly", alert: "readonly", fetch: "readonly", localStorage: "readonly" }
    },
    rules: {
      "no-undef": "error"
    }
  }
];
