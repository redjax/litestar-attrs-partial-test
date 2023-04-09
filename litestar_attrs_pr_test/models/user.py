import attrs
from typing import Union, Optional, Tuple, Dict, List
from uuid import UUID, uuid4


@attrs.define()
class User(object):
    first_name: str
    last_name: str
    id: UUID
