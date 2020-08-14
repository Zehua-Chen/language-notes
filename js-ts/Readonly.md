# Readonly

```ts
interface Props {
  readonly title: string;
}

let props: Props = { title: "" };

class Foo {
  readonly value: number;

  constructor() {
    this.value = 0;
  }
}
```

- TypeScript only
- Once applied to property, the property would be only writable during
  initialization
