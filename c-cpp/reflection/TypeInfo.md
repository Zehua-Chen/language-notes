# TypeInfo

- **Required header**: `#include <typeinfo>`
- `std::type_info` **contains type info**
  - Can only be instantiated as `const std::type_info &` (`std::type_info` does
    not have constructor, and assignment operator)
  - Obtained by using `typeid(T)` operator
- **RTTI** must be available
  - Clang: enabled by default

```cpp
#include <typeinfo>

struct foo {

};

int main() {
  const std::type_info t = typeid(foo);
  return 0;
}
```
