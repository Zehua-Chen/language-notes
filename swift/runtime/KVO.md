# Key Value Observing

- Only available on platforms where ObjC runtime is available
- Differenct from how it is done on ObjC

## Observed

- The observed property must be marked with the following
  - `@objc`
  - `dynamic`
- The observed object must
  - Inherit `NSObject`

## Observer

```swift
let observation = observed.observe(path, options: .new) { object, _ in }
```

- The observer don't have to inherit `NSObject`
- When the observatino object is deallocated, the observation stops
