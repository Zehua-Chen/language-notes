# Properties

## `get`, `set` Are Methods

- `get`, `set` blocks are considered as methods
- When properties are accessed, these methods would be called

```cs
using System.Runtime.CompilerServices;

struct Foo
{
  public int Value
  {
    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    get {}

    [MethodImpl(MethodImplOptions.AggressiveInlining)]
    set {}
  }
}
```

# Performance

- Trivial properties `public int F { get; set; }` still introduce function calls
- Use fields instead on hot code paths