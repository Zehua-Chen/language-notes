```rust
pub trait AsRef<T: ?Sized> {
  fn as_ref(&self) -> &T;
}

fn foo<Foo: AsRef<i32>>(foo: Foo) {
  // ...
}
```

Provides a way to convert conforming types to a certain reference type.

Note that here AsRef is just a generic constraint, that means `foo` can be
borrowed or owned
