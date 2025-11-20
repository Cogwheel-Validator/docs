const js = require('@eslint/js');
const tsParser = require('@typescript-eslint/parser');
const tsPlugin = require('@typescript-eslint/eslint-plugin');
const importPlugin = require('eslint-plugin-import');
const reactPlugin = require('eslint-plugin-react');
const reactHooksPlugin = require('eslint-plugin-react-hooks');
const nextPlugin = require('@next/eslint-plugin-next');

module.exports = [
  {
    ignores: [
      'next-env.d.ts',
      'node_modules/**',
      '.next/**',
      'mdx_gen/**'
    ]
  },
  // Base rules for all files
  {
    files: ['src/**/*.{js,jsx,cjs,mjs,ts,tsx,cts,mts}'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'module'
    },
    plugins: {
      import: importPlugin
    },
    rules: {
      ...js.rules,
      'prefer-object-has-own': 'error',
      'logical-assignment-operators': [
        'error',
        'always',
        { enforceForIfStatements: true }
      ],
      'no-else-return': ['error', { allowElseIf: false }],
      'no-lonely-if': 'error',
      'prefer-destructuring': [
        'error',
        { VariableDeclarator: { object: true } }
      ],
      'import/no-duplicates': 'error',
      'no-negated-condition': 'off',
      'prefer-regex-literals': ['error', { disallowRedundantWrapping: true }],
      'object-shorthand': ['error', 'always']
    }
  },
  // TypeScript files
  {
    files: ['src/**/*.{ts,tsx,cts,mts}'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        ecmaFeatures: {
          jsx: true
        },
        project: ['tsconfig.json', 'tsconfig.eslint.json']
      }
    },
    plugins: {
      '@typescript-eslint': tsPlugin
    },
    rules: {
      ...tsPlugin.configs.recommended.rules,
      '@typescript-eslint/prefer-for-of': 'error',
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/no-non-null-assertion': 'off',
      '@typescript-eslint/no-var-requires': 'off',
      '@typescript-eslint/ban-ts-comment': 'off',
      '@typescript-eslint/no-unnecessary-type-assertion': 'error',
      '@typescript-eslint/consistent-type-imports': 'error',
      '@typescript-eslint/non-nullable-type-assertion-style': 'error',
      '@typescript-eslint/prefer-optional-chain': 'error'
    }
  },
  // React and Next.js files
  {
    files: ['src/**/*.{jsx,tsx}'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        ecmaFeatures: {
          jsx: true
        }
      },
      globals: {
        React: 'readonly'
      }
    },
    plugins: {
      react: reactPlugin,
      'react-hooks': reactHooksPlugin,
      '@next/next': nextPlugin
    },
    rules: {
      ...reactPlugin.configs.recommended.rules,
      ...reactHooksPlugin.configs.recommended.rules,
      ...nextPlugin.configs.recommended.rules,
      'react/prop-types': 'off',
      'react/no-unknown-property': ['error', { ignore: ['jsx'] }],
      'react-hooks/exhaustive-deps': 'error',
      'react/self-closing-comp': 'error',
      'no-restricted-syntax': [
        'error',
        {
          selector:
            'CallExpression[callee.name=useMemo][arguments.1.type=ArrayExpression][arguments.1.elements.length=0]',
          message:
            '`useMemo` with an empty dependency array can\'t provide a stable reference, use `useRef` instead.'
        }
      ],
      'react/jsx-filename-extension': 'off',
      'react/jsx-curly-brace-presence': 'error',
      'react/jsx-boolean-value': 'error',
      '@next/next/no-html-link-for-pages': 'off'
    },
    settings: {
      react: { version: 'detect' }
    }
  },
  // TypeScript definition files
  {
    files: ['src/**/*.d.ts'],
    rules: {
      'no-var': 'off'
    }
  }
];
