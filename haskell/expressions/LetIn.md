# `let {assignments} in {expression}`

```haskell
foo a =
  let aa = a * a; b = 22
  in aa + b

-- gives 10022
foo 10
```

Define a set of assginments separated by `;` and use the assignments in
`expressions`
