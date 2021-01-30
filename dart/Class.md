# Inheritance

- Subclass does not have access to parent class's private members (`_` prefix)
  if the parent class belongs to another module

## Override

```dart
class Parent {
  void log() {}
}

class Child extends Parent {
  @override
  void log() {
    super.log()
  }
}
```

- Use `super` to access parent class's implementations
- Use `@override` to denote override

# Object

All class inherit from `Object` from `dart:core`

- `String toString()`: return string representation
- `int hashCode`: hash code
- `Type runtimeType`: runtime type
- `bool operator==(Object other)`: return true if `this` and `other` are the
  same instance
