# Lambda Expression

```java
I callable = (String s) -> {};
I callable = (s) -> {};
```

Lambda expressions do not form types themselves. Instead, anonymous classes
would be generated that implements the abstract type or interface that the
expression is assigned to.

- The abstract type or interface must only have one abstract function
