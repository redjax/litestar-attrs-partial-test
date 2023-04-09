from litestar import Litestar

from controllers.user import UserController

app = Litestar(route_handlers=[UserController])
