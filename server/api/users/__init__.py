from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute

from server.api.users.endpoints import Login, Refresh, Register

routes = [
    Route("/login", endpoint=Login),
    Route("/refresh", endpoint=Refresh),
    Route("/register", endpoint=Register)
]
