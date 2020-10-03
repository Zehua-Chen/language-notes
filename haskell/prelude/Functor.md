# Functor

```haskell
class Functor f where
  fmap :: (a -> b) -> f a -> f b
```

`fmap` (**required**) takes a function and a container, use the function to
transform the container and return a container of the same type

```haskell
data Container a = Container a
  deriving(Show, Eq)

instance Functor Container where
  fmap f (Container v) = Container (f v)
```

# `<$>`

```haskell
(<$>) :: Functor f => (a->b) -> f a -> f b
```

Infix version of `fmap`
