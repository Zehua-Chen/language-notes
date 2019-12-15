```rust
pub trait AsRef<T: ?Sized> {
    fn as_ref(&self) -> &T;
}

fn foo<Foo: AsRef<i32>>(foo: Foo) {
    // ...
}
```

Provides a way to convert conforming types to a certain reference type.

# Interesting Observation

- Take `foo` function above for example, both a value type and a reference
  type can be passed a parameter

  ```rust
  let var = /* */;

  foo(var); // OK
  foo(&var); // Still OK
  ```
