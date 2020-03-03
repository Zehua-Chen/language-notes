# Package

Packages are defined to be folders that contain

- `__init__.py`: the `index.js` equivalent in node.js

## Re-export From Modules

```py
from .module import A
```

- This **implicitly** re-export `A` from a module
  - This would trigger warnings with `mypy` when `--strict` is turned on
- To make this re-export implictly, add `__all__ = ["A"]` after the iports
