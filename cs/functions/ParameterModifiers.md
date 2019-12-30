# Parameter Modiifers

```cs
namespace Foo
{
  struct Boo {}

  class Program
  {
    static void Ref(ref Boo boo) {}
    static void In(in Boo boo) {}
    static void Out(out Boo boo) {}

    static void Main()
    {
      Boo boo;

      Ref(ref boo);
      Out(out boo);
      In(boo);
    }
  }
}
```

- All three parameter modifiers would cause the arguments to be passed by
  reference
- `ref`
  - The argument must be marked with `ref`
  - Argument must be initialized before passing
  - The function has the option to change the argument
- `out`
  - The argument must be marked with `out`
  - Argument do not have to be initialized
  - The function must initialize the argument
- `in`
  - The argument do not need special markings
  - The argument must be initialized before passing
  - For value types, the function cannot mutate the argument
  - For reference types, the function can mutate the object, but not the
    reference
