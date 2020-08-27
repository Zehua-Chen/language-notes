# Pattern Matching

```haskell
nthsq 1 = 1
nthsq n = 2 * n - 1 + nthsq (n - 1)
```

- When `nthsq` takes a parameter with value being `1`, the first definition is
  executed
- When `nthsq` takes a parameter with other values, the second definition is
  used

## Deconstruction

```haskell
mylength :: [a] -> Int
mylength [] = 0
mylength (x:xs) = 1 + mylength xs
```

Here `x:xs` deconstruct a linked list into

- `x`: the first element
- `xs`: the rest of the linked list
