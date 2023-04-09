## Notes

### Quoted annotations; using __future__.annotations and TYPE_CHECKING

When importing something (module, function) that would create a circular reference, you normally have to quote the type annotation. For example:

`def middleware_factory(*, app: "ASGIApp") -> "ASGIApp":`

`ASGIApp` is a module of `Litestar`. When creating an `app = Litestar()` object, using the `ASGIApp` type on `app` in `middleware_factory` would cause a circular reference, and the runtime would crash.

By using `if TYPE_CHECKING:`, we ensure that only static type checkers will detect the imported module (i.e. for autocomplete/intellisense, `mypy`, other static type checkers), but running the script will not import the module (as `TYPE_CHECKING` will never be `True`).

Example:

```
from __future__ import annotations

## Use TYPE_CHECKING to import modules that would create a circular reference
from typing import TYPE_CHECKING

#  i.e.:
#  if TYPE_CHECKING:
#    from module import script_that_imports_this_script
```