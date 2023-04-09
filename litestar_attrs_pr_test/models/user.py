## Import __future__.annotations, which quotes all anotations "behind the scenes"
from __future__ import annotations

## Use TYPE_CHECKING to import modules that would create a circular reference
from typing import TYPE_CHECKING

## TYPE_CHECKING is False in the parser, so this will not run, but the parser will understand bar.Bar
if TYPE_CHECKING:
    ## Put imports here that would cause runtime exceptions for circular imports.
    ...

import attrs
from typing import Union, Optional, Tuple, Dict, List
from uuid import UUID, uuid4


@attrs.define()
class User(object):
    first_name: str
    last_name: str
    id: UUID
