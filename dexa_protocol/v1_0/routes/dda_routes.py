from aiohttp import web
from aiohttp_apispec import docs, match_info_schema, querystring_schema
from dexa_protocol.v1_0.routes.maps.tag_maps import TAGS_DDA_LABEL
from dexa_protocol.v1_0.routes.openapi.schemas import (
    CreateDDATemplateRequestQueryStringSchema,
    DDATemplateMatchInfoSchema,
    DeactivateDDAMatchInfoSchema,
    ListDDAPublishedInMarketplaceQueryStringSchema,
    PublishDDAToMarketplaceMatchInfoSchema,
    QueryDDAInstancesQueryStringSchema,
    QueryDDATemplateQueryStringSchema,
    RequestDDAFromDataSourceMatchInfoSchema,
    UpdateDDATemplateQueryStringSchema,
)
from dexa_sdk.managers.dexa_manager import DexaManager
from dexa_sdk.utils import clean_and_get_field_from_dict
from mydata_did.v1_0.routes.maps.tag_maps import (
    TAGS_DATA_AGREEMENT_AUDITOR_FUNCTIONS_LABEL,
)
from mydata_did.v1_0.utils.util import str_to_bool


@docs(tags=[TAGS_DDA_LABEL], summary="Create a data disclosure agreement template.")
@querystring_schema(CreateDDATemplateRequestQueryStringSchema())
async def create_data_disclosure_agreement_handler(request: web.BaseRequest):
    """
    Request handle to create a data disclosure agreement template.

    Args:
        request: aiohttp request object

    """
    context = request.app["request_context"]

    # Fetch query string params
    publish_flag = str_to_bool(
        clean_and_get_field_from_dict(request.query, "publish_flag")
    )

    da_template_id = clean_and_get_field_from_dict(request.query, "da_template_id")

    # Initialise DEXA manager
    manager = DexaManager(context)

    # Create and store DDA in wallet.
    record = await manager.create_and_store_dda_template_in_wallet(
        da_template_id, publish_flag=publish_flag
    )

    return web.json_response(record.serialize())


@docs(tags=[TAGS_DDA_LABEL], summary="Query data disclosure agreement templates.")
@querystring_schema(QueryDDATemplateQueryStringSchema())
async def query_dda_handler(request: web.BaseRequest):
    """
    Request handle to query data disclosure agreement templates.

    Args:
        request: aiohttp request object

    """
    context = request.app["request_context"]

    # Fetch query string params
    template_id = clean_and_get_field_from_dict(request.query, "template_id")
    template_version = clean_and_get_field_from_dict(request.query, "template_version")
    industry_sector = clean_and_get_field_from_dict(request.query, "industry_sector")
    publish_flag = clean_and_get_field_from_dict(request.query, "publish_flag")
    delete_flag = clean_and_get_field_from_dict(request.query, "delete_flag")
    latest_version_flag = clean_and_get_field_from_dict(
        request.query, "latest_version_flag"
    )
    page = clean_and_get_field_from_dict(request.query, "page")
    page = int(page) if page is not None else page
    page_size = clean_and_get_field_from_dict(request.query, "page_size")
    page_size = int(page_size) if page_size is not None else page_size

    # Initialise DEXA manager
    manager = DexaManager(context)

    # Create and store DDA in wallet.
    paginationResult = await manager.query_dda_templates_in_wallet(
        template_id=template_id,
        template_version=template_version,
        industry_sector=industry_sector,
        publish_flag=publish_flag,
        delete_flag=delete_flag,
        latest_version_flag=latest_version_flag,
        page=page if page else 1,
        page_size=page_size if page_size else 10,
    )

    return web.json_response(paginationResult._asdict())


@docs(tags=[TAGS_DDA_LABEL], summary="Update DDA template.")
@match_info_schema(DDATemplateMatchInfoSchema())
@querystring_schema(UpdateDDATemplateQueryStringSchema())
async def update_dda_template_handler(request: web.BaseRequest):
    """Update DDA template."""

    # Request context
    context = request.app["request_context"]

    # Path params
    template_id = request.match_info["template_id"]

    # Query string params
    publish_flag = clean_and_get_field_from_dict(request.query, "publish_flag")
    publish_flag = str_to_bool(publish_flag)

    # Initialise MyData DID Manager
    manager = DexaManager(context=context)

    record = await manager.update_dda_template_in_wallet(
        template_id=template_id, publish_flag=publish_flag
    )

    return web.json_response(record.serialize(), status=200)


@docs(tags=[TAGS_DDA_LABEL], summary="Delete DDA template.")
@match_info_schema(DDATemplateMatchInfoSchema())
async def delete_dda_template_handler(request: web.BaseRequest):
    """Delete DDA template in wallet"""

    # Request context
    context = request.app["request_context"]

    # Path params
    template_id = request.match_info["template_id"]

    # Initialise MyData DID Manager
    manager = DexaManager(context=context)

    await manager.delete_dda_template_in_wallet(template_id)

    return web.json_response({}, status=204)


@docs(tags=[TAGS_DDA_LABEL], summary="Publish DDA template.")
@match_info_schema(DDATemplateMatchInfoSchema())
async def publish_dda_template_handler(request: web.BaseRequest):
    """Publish DDA template in wallet"""

    # Request context
    context = request.app["request_context"]

    # Path params
    template_id = request.match_info["template_id"]

    # Initialise MyData DID Manager
    manager = DexaManager(context=context)

    await manager.publish_dda_template_wallet(template_id)

    return web.json_response({}, status=204)


@docs(tags=[TAGS_DDA_LABEL], summary="Publish DDA to marketplace")
@match_info_schema(PublishDDAToMarketplaceMatchInfoSchema())
async def publish_dda_to_marketplace_handler(request: web.BaseRequest):
    """Publish DDA to marketplace handler"""

    # Request context
    context = request.app["request_context"]

    # Path params
    template_id = request.match_info["template_id"]
    connection_id = request.match_info["connection_id"]

    # Initiatlise MyData DID manager
    mgr = DexaManager(context)

    record = await mgr.publish_dda_template_to_marketplace(connection_id, template_id)

    return web.json_response(record.serialize())


@docs(tags=[TAGS_DDA_LABEL], summary="List DDA published in marketplace.")
@querystring_schema(ListDDAPublishedInMarketplaceQueryStringSchema())
async def list_dda_published_in_marketplace(request: web.BaseRequest):
    """List DDA published in marketplace"""

    # Request context
    context = request.app["request_context"]

    # Query string params
    page = clean_and_get_field_from_dict(request.query, "page")
    page = int(page) if page is not None else page
    page_size = clean_and_get_field_from_dict(request.query, "page_size")
    page_size = int(page_size) if page_size is not None else page_size

    # Initiatlise MyData DID manager
    mgr = DexaManager(context)

    # Paginated list of published DDAs
    pagination_result = await mgr.list_dda_published_in_marketplace(
        page if page else 1, page_size if page_size else 10
    )

    return web.json_response(pagination_result._asdict())


@docs(tags=[TAGS_DDA_LABEL], summary="Request DDA offer from Data Source.")
@match_info_schema(RequestDDAFromDataSourceMatchInfoSchema())
async def request_dda_offer_from_ds_handler(request: web.BaseRequest):
    """Request DDA offer from DS handler

    Args:
        request (web.BaseRequest): Request
    """

    # Request context
    context = request.app["request_context"]

    # Path params.
    template_id = request.match_info["template_id"]
    connection_id = request.match_info["connection_id"]

    # Initialise manager.
    mgr = DexaManager(context)

    # Request DDA from DS.
    await mgr.request_dda_offer_from_ds(connection_id, template_id)

    return web.json_response({}, status=204)


@docs(tags=[TAGS_DATA_AGREEMENT_AUDITOR_FUNCTIONS_LABEL], summary="Query DDA instances")
@querystring_schema(QueryDDAInstancesQueryStringSchema())
async def query_dda_instances_handler(request: web.BaseRequest):
    """
    Request handler for querying DDA instances.
    """

    # Context
    context = request.app["request_context"]

    instance_id = clean_and_get_field_from_dict(request.query, "instance_id")
    template_id = clean_and_get_field_from_dict(request.query, "template_id")
    template_version = clean_and_get_field_from_dict(request.query, "template_version")
    connection_id = clean_and_get_field_from_dict(request.query, "connection_id")
    page = clean_and_get_field_from_dict(request.query, "page")
    page = int(page) if page is not None else page
    page_size = clean_and_get_field_from_dict(request.query, "page_size")
    page_size = int(page_size) if page_size is not None else page_size

    # Initialise Dexa manager
    manager = DexaManager(context=context)

    # Get the data agreement instances
    paginationResult = await manager.query_dda_instances(
        instance_id,
        template_id,
        template_version,
        connection_id,
        page if page else 1,
        page_size if page_size else 10,
    )

    return web.json_response(paginationResult._asdict())


@docs(tags=[TAGS_DDA_LABEL], summary="Deactivate DDA.")
@match_info_schema(DeactivateDDAMatchInfoSchema())
async def deactivate_dda_instance_handler(request: web.BaseRequest):
    """Deactivate DDA instance.

    Args:
        request (web.BaseRequest): Request.
    """

    # Context
    context = request.app["request_context"]

    # Path parameters
    instance_id = request.match_info["instance_id"]

    # Initialise manager.
    mgr = DexaManager(context)

    # Call the function.
    await mgr.send_deactivate_dda_message(instance_id)

    return web.json_response({}, status=204)
