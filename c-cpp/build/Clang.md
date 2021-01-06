# GCC Compatibility

Clang is compatibile with GCC unless otherwise specified

# Target

```
clang main.c -o app_x86 -target x86_64-apple-macos10.12
clang main.c -o app_arm -target arm64-apple-macos11
```

- Specified using `-target` flag
- Architecture is part of the target

Format of targets can be found on
[clang.llvm.org](https://clang.llvm.org/docs/CrossCompilation.html#general-cross-compilation-options-in-clang)

- `abi` is optional

# Inline

```cpp
struct foo {
  float value;

  __attribute__((always_inline))
  inline foo operator+(const foo &f) const {
    return {value + f.value};
  }
};

foo boo(foo &a, foo &b) {
  return a + b;
}
```

`__attribute__((always_inline))` would always inline a function **regardless
of optimization settings**
