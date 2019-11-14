# Reference Coersion

Given a reference to a type `A`, and a parameter that is a reference
to a type `B`, rust would automatically convert the reference of
type `A` to a reference of type `B` if `A`'s implementation of
`trait Deref` can convert a reference of `A` to that of `B`

Mutable references can be converted to

- `&mut T` if `DerefMut<Target = T>`
- `& T` if `Deref<Target = T>`

Immutable references can only be converted to immutable references

```rust
fn print_number(number: &i32) {
    println!("number = {}", number);
}

fn main() {
    let mut value = Box::new(12);

    println!("value = {}", value);
    println!("*value = {}", *value);

    let value_ref = value.as_mut();
    *value_ref = 22;

    print_number(&value);
}
```

Here, `struct Box<T>` implements `Deref` that can convert
to references of `i32`. Therefore, `&value` can be convert to
a reference to `i32`