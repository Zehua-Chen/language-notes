# Static Import

```java
import static java.lang.System.out;

public class Program {
  public static void main(String[] args) {
    out.println("main()");
  }
}
```

Static imports allows the use of static properties and methods without using the
class name;

- `import static package.Class.symbol`: would allow the use of `symbol` without
  class name
- `import` **must refer to package name**;
