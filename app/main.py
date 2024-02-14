from api.customer import route as customer_route
from fastapi import FastAPI


def app_factory(routes) -> FastAPI:
    """Create a FastAPI app object"""

    app = FastAPI()

    for route in routes:
        app.add_api_route(route)

    return app


app = app_factory([customer_route])
