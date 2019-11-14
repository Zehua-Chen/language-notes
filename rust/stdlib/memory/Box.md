# Smart Pointer

```rust
struct Box<T>
```

Box is a smart pointer type in rust

- Manages some heap memory
- Release the heap memory when it goes out of scope
- Provides a way to refer to a type of unknown size (polymorphism)

# Factory Functions

```rust
impl Box<T> {
    fn new(v: T) -> Box<T>
}
```

Initialize a box to a given value

```rust
impl Box<T> {
    fn new_uninit() -> Box<T>
}
```

Create a box without initializing its memory

# Methods

```rust
impl Box<T> {
    fn as_mut(&mut self) -> &mut T
}
```

Obtain a mutable reference to the content of the box

- Note to write to this memory, use `*reference = value;` syntax
