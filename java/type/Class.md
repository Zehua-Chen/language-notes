# Files

Each `Class.java` can only contain **one public class named `Class`**

- There is no restrictions on non public classes

# Member Variables

## `final`

```java
public class Foo {
  final String value;

  public Foo() {
    value = "Foo";
  }
}
```

Member variables marked with `final` are only writable in the constructor
