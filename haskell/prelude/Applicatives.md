# Applicatives

```haskell
class (Functor f) => Applicative f where
  pure a :: a -> f a
  f (a - > b) <*> f a :: f b
```
