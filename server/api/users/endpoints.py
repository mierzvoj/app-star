from starlette import status
from starlette.applications import Starlette
from starlette.concurrency import run_in_threadpool
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from starlette.routing import Mount, Route
from starlette.types import Message, Receive, Scope, Send
from starlette.websockets import WebSocket
import main


class Login(HTTPEndpoint):
    async def post(self, request):
        json = await request.json()
        print(json)
        return PlainTextResponse("post")


class Register(HTTPEndpoint):
    pass


class Refresh(HTTPEndpoint):
    pass

