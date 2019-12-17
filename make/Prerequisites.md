# Order Only Prerequisites

```make
target: normals | order-only
    command
```

Make will only satisfy order prerequisites when the prerequisites does not
exist. If the item already exists, make wont' satisfy it again even though the
item is newer than the target
