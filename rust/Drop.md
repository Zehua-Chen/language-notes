# Drop

```rust
trait Drop {
    fn drop(&mut self);
}
```

When the drop is implemented for a type, as an instance of this type
goes out of scope, the `fn drop(&mut self)` will be called to perform
cleanup

## Explicitly Drop

```rust
pub mod std {
    pub mod mem {
        pub fn drop<T>(_x: T)
    }
}
```

This **function** explictly invoke the drop **method** of a type.

The `drop` **method** cannot be called by the user because the compiler also
invokes this method. The user calling this method would cause a double
free error.
