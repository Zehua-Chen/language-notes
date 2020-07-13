# Tuple

- Tuples created with the parenthesis syntax are of type `ValueTuple<...>` to
  improve performance in hot code paths
- To convert a value tuple to a reference tuple (`class Tuple`), use `ToTuple()`
  on `ValueTuple`
- Tuple types implement `IEquatable` and `IComparable`

## Unnamed Tuple

```cs
var tuple = ("Peter", 20);
Console.WriteLine(tuple.Item1);
```

## Named Tuple

```cs
var tuple = (Name: "Peter", Age: 20);
Console.WriteLine(tuple.Name);
```
