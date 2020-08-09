# `new` operator

```cpp
#include <cstddef.h>

struct object {
  void *operator new(std::size_t size);
}

```

- Used during `new object`;
