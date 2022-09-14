from aiohttp import web
from dexa_protocol.v1_0.routes.maps.route_maps import MARKETPLACE_ROUTES, ROUTES_DDA
from dexa_protocol.v1_0.routes.maps.tag_maps import TAGS_DDA


async def register(app: web.Application):
    """Register routes."""

    app.add_routes(ROUTES_DDA)
    app.add_routes(MARKETPLACE_ROUTES)


def post_process_routes(app: web.Application):
    """Amend swagger API."""

    # Add top-level tags description
    if "tags" not in app._state["swagger_dict"]:
        app._state["swagger_dict"]["tags"] = []

    app._state["swagger_dict"]["tags"].append(TAGS_DDA)
