# TS Module

```ts
module Foo {}
```

- Can be merged across files
- When the file contains an `export` keyword, then all modules in the file would
  not be automatically visible unless exported

## Ambient Module

```ts
declare module X {}

declare module "path" {
  export interface Foo {}
}

// other file
import { Foo } from "path";
```

- Ambient modules contain only declarations
- When the name of an ambient module is in `""`, then the declarations can be
  imported as if they are from a file (es6 module)
