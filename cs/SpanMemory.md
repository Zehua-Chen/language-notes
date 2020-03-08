# Overview

- All types mentioned here are put under `namespace System`

# Span

`Span<T>` provides a type safe and memory safe access to a contiguous region of
memory

- `Span<T>` is a ref struct: can only be put on stack
- `ReadOnlySpan<T>` is a read only variant that can be used to avoid implicit
  copies when used with `in` operator

# Memory

`Memory<T>` is similar to `Span<T>` but can be put on heap

- `ReadOnlyMemory<T>` is a read only variant that can be used to avoid implicit
  copies when used with `in` operator
