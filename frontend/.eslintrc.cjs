/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution')

module.exports = {
  rules: {"vue/no-multiple-template-root": "off" },
  root: true,
  'extends': [
    'plugin:vue/vue3-essential',
    'eslint:recommended',
    '@vue/eslint-config-typescript'
  ],
  parserOptions: {
    ecmaVersion: 'latest'
  }
}
