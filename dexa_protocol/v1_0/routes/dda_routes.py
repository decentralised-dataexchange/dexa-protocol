from aiohttp import web
from aiohttp_apispec import (
    docs,
    request_schema,
    querystring_schema,
    match_info_schema
)
from dexa_sdk.managers.dexa_manager import DexaManager
from dexa_sdk.utils import clean_and_get_field_from_dict
from mydata_did.v1_0.utils.util import str_to_bool
from .maps.tag_maps import TAGS_DDA_LABEL
from .openapi.schemas import (
    CreateDataDisclosureAgreementTemplateRequestSchema,
    CreateDDATemplateRequestQueryStringSchema,
    PublishDDAToMarketplaceMatchInfoSchema,
    QueryDDATemplateQueryStringSchema,
    UpdateDDATemplateQueryStringSchema,
    DDATemplateMatchInfoSchema,
    UpdateDDATemplateRequestSchema
)


@docs(tags=[TAGS_DDA_LABEL], summary="Create a data disclosure agreement template.")
@querystring_schema(CreateDDATemplateRequestQueryStringSchema())
@request_schema(CreateDataDisclosureAgreementTemplateRequestSchema())
async def create_data_disclosure_agreement_handler(request: web.BaseRequest):
    """
    Request handle to create a data disclosure agreement template.

    Args:
        request: aiohttp request object

    """
    context = request.app["request_context"]

    # Fetch request body
    dda = await request.json()

    # Fetch query string params
    publish_flag = str_to_bool(clean_and_get_field_from_dict(request.query, "publish_flag"))

    # Initialise DEXA manager
    manager = DexaManager(context)

    # Create and store DDA in wallet.
    record = await manager.create_and_store_dda_template_in_wallet(
        dda,
        publish_flag=publish_flag
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
    latest_version_flag = clean_and_get_field_from_dict(request.query, "latest_version_flag")
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
        page_size=page_size if page_size else 10
    )

    return web.json_response(paginationResult._asdict())


@docs(tags=[TAGS_DDA_LABEL], summary="Update DDA template.")
@match_info_schema(DDATemplateMatchInfoSchema())
@querystring_schema(UpdateDDATemplateQueryStringSchema())
@request_schema(UpdateDDATemplateRequestSchema())
async def update_dda_template_handler(request: web.BaseRequest):
    """Update DDA template."""

    # Request context
    context = request.app["request_context"]

    # Path params
    template_id = request.match_info["template_id"]

    # Request body
    dda = await request.json()

    # Query string params
    publish_flag = clean_and_get_field_from_dict(request.query, "publish_flag")
    publish_flag = str_to_bool(publish_flag)

    # Initialise MyData DID Manager
    manager = DexaManager(context=context)

    record = await manager.update_dda_template_in_wallet(
        template_id=template_id,
        dda=dda,
        publish_flag=publish_flag
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

    await manager.delete_dda_template_in_wallet(
        template_id
    )

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

    await manager.publish_dda_template_wallet(
        template_id
    )

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

    record = await mgr.publish_dda_template_to_marketplace(
        connection_id,
        template_id
    )

    return web.json_response(record.serialize())
