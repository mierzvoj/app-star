import asyncio
import json
import typing

from starlette import status
from starlette.concurrency import run_in_threadpool
from starlette.endpoints import HTTPEndpoint
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from starlette.routing import Mount
from starlette.types import Message, Receive, Scope, Send
from starlette.websockets import WebSocket



class Login(HTTPEndpoint):
    pass


class Register(HTTPEndpoint):
    pass


class Refresh(HTTPEndpoint):
    pass
