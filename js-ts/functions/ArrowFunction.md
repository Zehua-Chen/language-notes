# As Class Fields

```ts
class Foo {
  callback = () => {
    console.log("callback");
  };
}
```

- The entire function is stored as a field in the object
- To optimize
  - Use `.bind()` function
  - Use `@babel/plugin-transform-arrow-functions` to transform arrow functions
    to `.bind()` functions
