# Clang

## Target

```
clang main.c -o app_x86 -target x86_64-apple-macos10.12
clang main.c -o app_arm -target arm64-apple-macos11
```

- Specified using `-target` flag
- Architecture is part of the target

Format of targets can be found on
[clang.llvm.org](https://clang.llvm.org/docs/CrossCompilation.html#general-cross-compilation-options-in-clang)

- `abi` is optional
