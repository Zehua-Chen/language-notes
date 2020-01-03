# Conditional Implementation

```rust
impl<T: TraitA + TraitB> Type<T> {}
```

Implementations inside the block is conditionally available when the generic
parameter implements `TraitA` and `TraitB`
