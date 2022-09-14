from aiohttp import web
from aiohttp_apispec import docs, match_info_schema, querystring_schema
from dexa_protocol.v1_0.routes.maps.tag_maps import TAGS_MARKETPLACE_LABEL
from dexa_protocol.v1_0.routes.openapi.schemas import (
    AddMarketPlaceConnectionMatchInfoSchema,
    QueryMarketplaceConnectionsQueryInfoSchema,
    QueryPublishedDDATemplatesForMarketplaceConnectionMatchInfoSchema,
    QueryPublishedDDATemplatesQueryString,
)
from dexa_sdk.managers.dexa_manager import DexaManager
from dexa_sdk.utils import clean_and_get_field_from_dict


@docs(tags=[TAGS_MARKETPLACE_LABEL], summary="Mark a connection as data marketplace")
@match_info_schema(AddMarketPlaceConnectionMatchInfoSchema())
async def add_marketplace_connection_handler(request: web.BaseRequest):
    """Mark connection as marketplace handler"""

    # Request context
    context = request.app["request_context"]

    # Path params
    connection_id = request.match_info["connection_id"]

    # Initialise MyData DID Manager
    manager = DexaManager(context=context)

    record = await manager.add_marketplace_connection(connection_id)

    return web.json_response(record.serialize())


@docs(tags=[TAGS_MARKETPLACE_LABEL], summary="Query marketplace connections")
@querystring_schema(QueryMarketplaceConnectionsQueryInfoSchema())
async def query_marketplace_connections_handler(request: web.BaseRequest):
    """Query marketplace connections handler"""

    # Request context
    context = request.app["request_context"]

    # Query params
    connection_id = clean_and_get_field_from_dict(request.query, "connection_id")

    # Initialise MyData DID Manager
    manager = DexaManager(context=context)

    pagination_result = await manager.query_marketplace_connections(
        connection_id=connection_id
    )

    return web.json_response(pagination_result._asdict())


@docs(tags=[TAGS_MARKETPLACE_LABEL], summary="Query published DDA templates.")
@querystring_schema(QueryPublishedDDATemplatesQueryString())
async def query_published_dda_template_handler(request: web.BaseRequest):
    """Query publish DDA template handler.

    Args:
        request (web.BaseRequest): Request.
    """

    # Request context
    context = request.app["request_context"]

    # Query string params
    page = clean_and_get_field_from_dict(request.query, "page")
    page = int(page) if page is not None else page
    page_size = clean_and_get_field_from_dict(request.query, "page_size")
    page_size = int(page_size) if page_size is not None else page_size

    # Initialise MyData DID Manager
    manager = DexaManager(context=context)

    # Query the records and obtain the paginated result.
    results = await manager.query_publish_dda_template_records(
        page if page else 1, page_size if page_size else 10
    )

    return web.json_response(results._asdict())


@docs(
    tags=[TAGS_MARKETPLACE_LABEL],
    summary="Query published DDA tempates for a marketplace connection",
)
@match_info_schema(QueryPublishedDDATemplatesForMarketplaceConnectionMatchInfoSchema())
async def query_publish_dda_template_for_marketplace_connection(
    request: web.BaseRequest,
):
    """Query published DDA templates for a marketplace connection.

    Args:
        request (web.BaseRequest): Request
    """

    # Request context
    context = request.app["request_context"]

    # Path params
    connection_id = request.match_info["connection_id"]

    # Initialise the manager
    mgr = DexaManager(context)

    pagination_result = await mgr.send_list_marketplace_dda_message(connection_id)

    return web.json_response(pagination_result._asdict())
