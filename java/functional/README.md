# Lambda Expression

```java
interface Foo {
  // Can only have one method
  void accept(String s);
}

Foo callable = (String s) -> {};
Foo callable = (s) -> {};
```

Lambda expressions do not form types themselves. Instead, anonymous classes
would be generated that implements the abstract type or interface that the
expression is assigned to.

- The abstract type or interface must only have one method

# Consumer, Supplier, Function, Predicate

Package `java.util.function`

- `Consumer<T>` takes a value of `T` but does not return anything
- `Function<T, R>` takes a value of `T` and return a value of `R`
- `Supplier<T, R>` returns the value of `R`
- `Predicate<T>`: a `Function` that returns a boolean

Lambda expression can be used to generate conforming types to these interfaces
