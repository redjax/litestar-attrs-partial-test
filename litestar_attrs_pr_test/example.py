## Import __future__.annotations, which quotes all anotations "behind the scenes"
from __future__ import annotations

## Use TYPE_CHECKING to import modules that would create a circular reference
from typing import TYPE_CHECKING

#  i.e.:
#  if TYPE_CHECKING:
#    from module import script_that_imports_this_script

import logging
from litestar import Litestar, get, Request
from litestar.datastructures import State

import attrs
from typing import Optional, Any, Dict, List, Union, cast

from controllers.user import UserController

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

## TYPE_CHECKING is False in the parser, so this will not run, but the parser will understand bar.Bar
if TYPE_CHECKING:
    from litestar.types import ASGIApp, Receive, Scope, Send


logger = logging.getLogger(__name__)


@attrs.define()
class AppSettings(object):
    DATABASE_URI: str = "sqlite+aiosqlite:///database.db"


settings = AppSettings()


def set_state_on_startup(state: State) -> None:
    ...


## The "ASGIApp" type annotation would normally be quoted.
#  https://docs.litestar.dev/2/usage/the-litestar-app.html#id6
#    This is not necessary by importing __future__.annotations
def middleware_factory(*, app: ASGIApp) -> ASGIApp:
    async def my_middleware(scope: "Scope", receive: "Receive", send: "Send") -> None:
        state = scope["app"].state
        logger.info(f"State value in middleware: {state.value}")
        await app(scope, receive, send)

    return my_middleware


def my_dependency(state: State) -> Any:
    """
    Dependencies can receive state via injection.
    """
    logger.info(f"State value in dependency: {state.value}")


@get("/")
def hello_world() -> Dict[str, str]:
    return {"hello": "world"}


def get_db_connection(state: "State") -> AsyncEngine:
    """
    Returns db engine.
    """

    if not getattr(state, "engine", None):
        state.engine = create_async_engine(settings.DATABASE_URI)

    return cast("AsyncEngine", state.engine)


async def close_db_connection(state: State) -> None:
    """
    Close db connection stored in application State object.
    """

    if getattr(state, "engine", None):
        await cast("AsyncEngine", state.engine).dispose()


app = Litestar(
    on_startup=[get_db_connection],
    route_handlers=[UserController],
    on_shutdown=[close_db_connection],
)
