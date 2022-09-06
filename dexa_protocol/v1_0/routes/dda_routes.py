from aiohttp import web
from aiohttp_apispec import docs, request_schema
from marshmallow import EXCLUDE

from dexa_sdk.agreements.dda.v1_0.models import (
    DataDisclosureAgreementSchema,
)
from .maps.tag_maps import TAGS_DDA_LABEL


class WrappedDataDisclosureAgreementSchema(DataDisclosureAgreementSchema):
    class Meta:
        """OpenAPISchema metadata."""

        # Hack to use child classes of BaseModelSchema
        # as OpenAPI request schema
        model_class = dict

        # Exclude unknown fields
        unknown = EXCLUDE


@docs(tags=[TAGS_DDA_LABEL], summary="Create a Data Disclosure Agreement")
@request_schema(WrappedDataDisclosureAgreementSchema())
async def create_data_disclosure_agreement_handler(request: web.BaseRequest):
    """
    Request handle to create a data disclosure agreement.

    Args:
        request: aiohttp request object

    """
    context = request.app["request_context"]

    # Fetch request body
    data_agreement = await request.json()

    return web.json_response(
        {"purposeDescription": data_agreement["purposeDescription"]}
    )
