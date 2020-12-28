# `@autoclosure`

```swift
func foo(value: @autoclosure () -> Int) {
  print(value())
}
```

`@autoclosure` automatically convert a expression to be a closure

- **For callers**, the parameter would have the type of the return type of the
  closure (ex. `Int`)
- **Inside the function**, the parameter would still be a closure
