# `let {assignments} in {expression}`

```haskell
foo x =
  let constant = 17
    in constant + x

main = do
  -- gvies 27
  putStrLn (show (foo 10))
```

Define a set of assginments separated by `;` and use the assignments in
`expressions`. **The `expression` would be the output of the "let in"
statement**
