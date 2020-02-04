# Anonymous Classes

Given a type T that is one of the following

- Interface
- Class

an anonymous can be created that either implements or extends the given `T`

```java
T name = new T {
  // implementations, overrides
};
```

Inside the implementation or overrides, values from the outer scope can be
captured
