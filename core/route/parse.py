import io

from ..conf import settings
from ..request import Request
from .routes import get_routes


def parse_environment(environment, start_response):
    headers = [("Content-Type", "text/html")]
    start_response("200 Ok", headers)
    request = Request(environment, start_response)

    routes = get_routes(settings.ROUTES)
    response_string = routes.get(request.path, lambda x: "Hello World")(request)
    response = io.BytesIO(response_string.encode("utf-8"))
    return response