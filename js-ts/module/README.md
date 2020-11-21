# Modules

- ES2015 module (`import a from "./foo"`)
- TS module (`module {}`)
- TS namespace (`namespace {}`)

# ES 2015 Module

## `import`

## Absolute Import

Absolute import does not start with `.` or `..`

```ts
import Foo from "components/Foo";
import Boo from "third-party";
```

### TypeScript

#### `node_modules`

Typescript has two modes of finding modules `classic` and `node`. **TypesScript
uses `classic` by default.**

```json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}
```

More details can be found in
[Typescript handbook](https://www.typescriptlang.org/docs/handbook/module-resolution.html#node)

- **if working with modules under `node_modules`, set the value to `node`**

#### Others

`tsconfig.json` contains two settings for enabling non-`node_modules` absolute
imports

```json
{
  "compilerOptions": {
    // Base directory to resolve non-absolute module names.
    "baseUrl": "./",
    // A series of entries which re-map imports to lookup locations relative
    // to the 'baseUrl'
    "paths": {
      "*": ["src/*"]
    }
  }
}
```

### File Extension

In some environments (browser, node), modules must be imported with their
extensions

```ts
import { boo } from "./foo.js";

boo();
```

Given `foo.ts`, TypeScript allows the file to be imported as `foo.js`

# TS Module vs TS Namespace

Similarity:

- Merged across files

Difference:

- TS modules can be used to augment ES6 modules
