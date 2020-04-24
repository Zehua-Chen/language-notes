ValueTask

void Foo(Boo boo = default)

Local function
int Compute() => ...

Overload Disambiguate + Optional parameter
Compute(label: 12)

Generic Constraint
- Delegate
- Enum
- `unmanaged` (pointers)

Tuple, ValueTuple
(a, b), == !=

Ref
ref int a = ref Foo();
ref readonly int a = ref Foo();

int c = a
a = ref c;

ref readonly int Foo(int a)
{
  return ref a;
}

Span
span indexer returns refs

stackalloc
Span<int> s = stackalloc int[];

swich (a)
{
  case TypeA aa:
  case TypeB ab:
  case _:
}

return a switch
{
  case ... => value,
  case ... => value,
  ... when value == value => value,
  Type { P: value, PP: var pp } t => value,
  _ => value,
};

Deconstructor with switch

Type (_ var a, var b) =>

array[^1] grab last one

IAsyncEnumerable

unchecked {}

ZString
