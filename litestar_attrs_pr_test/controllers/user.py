from uuid import UUID, uuid4
from typing import Union, List, Dict, Optional, Any
from litestar import Controller, get, post, put, patch, delete
from litestar.partial import Partial
from models.user import User

import attrs


# @attrs.define()
class UserController(Controller):
    path: str = "/users"

    @post()
    async def create_user(self, data: User) -> User:
        ...

    @get()
    async def list_users(self) -> List[User]:
        ...

    @patch(path="/{user_id:uuid}")
    async def partial_update_user(self, user_id: UUID, data: Partial[User]) -> User:
        ...

    @put(path="/{user_id:uuid}")
    async def update_user(self, user_id: UUID, data: User) -> User:
        ...

    @get(path="/{user_id:uuid}")
    async def get_user(self, user_id: UUID) -> User:
        ...

    @delete(path="/{user_id:uuid}")
    async def delete_user(self, user_id: UUID) -> None:
        ...
