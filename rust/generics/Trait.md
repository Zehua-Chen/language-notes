# Trait

```rust
trait Name {
    fn declare();
    fn implement() {}
}
```

- Traits define a set of shared behavior between multiple structures
  - Conforming structures have to implement those behaviors
- Traits can contain default implementations
- To use contents of a trait, the trait needs to be used

# Trait As Return Type

- Functions can return trait type rather than a concrete type
- Functions can only return one type of implementing type
