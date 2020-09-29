# Monad

Monad is a class

```haskell
class Monad m where
  (>>=) :: m a -> (a -> m b) -> m b
  (>>) :: m a -> m b -> m b
  return :: a -> m a
  fail :: String -> m a
```

- `return` takes a a value and put the value inside the container
- `>>=` (bind): transform a monad containing type `a` to a monad containing type
  `b`
- `>>` (then): takes two monad and returns the second monad
- `fail`: error handling

## `>>`

```haskell
main =
  putStrLn "first" >>
  putStrLn "second"
```

# `do`

```haskell
main = do
  putStrLn "a"
  putStrLn "b"
  -- equivalenet to
  -- putStrLn "a" >>
  -- putStrLn "b"

  a <- foo
  putStrLn a
  -- equivalenet to
  -- foo >>= \(a ->
  -- putStrlln a)
```
