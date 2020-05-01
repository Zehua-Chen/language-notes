# Type of Methods

```cpp
// Belongs to type Foo, takes two int parameters and returns one parameter
int (Foo::)(int, int)
```

## Type of Method Pointers

```cpp
int (Foo::*)(int, int)
int (Foo::&)(int, int)
```

# Method Pointers

```cpp
int (Foo::*foo_pointer)(int, int);
int (Foo::&foo_ref)(int, int);
```

## Invoking Method Pointers

```cpp
(pointer->*func_pointer)(parameters);
```
