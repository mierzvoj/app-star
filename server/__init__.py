import uvicorn
from starlette.applications import Starlette
from starlette.routing import Mount
from server.api.users import routes as users_routes
routes = [
    Mount("/api", routes=users_routes, name="api"),
]


def run():
    app = Starlette(debug=True, routes=routes)
    uvicorn.run(app)
    print("uvi started")
