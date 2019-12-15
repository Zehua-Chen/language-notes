# `ref` Pattern

When pattern matching or destructuring,

- `ref`
- `ref mut`

key words/phrases can be used to take reference of the matched or
extracted values

## Example

```rust
let o = /* Option<i32> */

match o {
    Some(ref mut value) => {}
    None => {}
}
```

Here `value` would have type `&mut i32`
