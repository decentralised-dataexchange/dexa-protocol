import typing

from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from marshmallow import EXCLUDE, fields


class ListMarketplaceDDAResponseModel(BaseModel):
    class Meta:
        # Schema class
        schema_class = "ListMarketplaceDDAResponseModelSchema"

    def __init__(
        self,
        *,
        dda: dict,
        template_id: str,
        industry_sector: str,
        connection_url: str,
        created_at: str,
        updated_at: str,
        **kwargs
    ):
        # Pass args to parent constructor
        super().__init__(**kwargs)

        # Set model attributes.
        self.dda = dda
        self.template_id = template_id
        self.industry_sector = industry_sector
        self.connection_url = connection_url
        self.updated_at = updated_at
        self.created_at = created_at


class ListMarketplaceDDAResponseModelSchema(BaseModelSchema):
    class Meta:
        # Model class
        model_class = ListMarketplaceDDAResponseModel

        # Unknown fields are excluded
        unknown = EXCLUDE

    dda = fields.Dict()
    template_id = fields.Str()
    industry_sector = fields.Str()
    connection_url = fields.Str()
    updated_at = fields.Str()
    created_at = fields.Str()


class ListMarketplaceDDAResponseBody(BaseModel):
    class Meta:
        # Schema class
        schema_class = "ListMarketplaceDDAResponseBodySchema"

    def __init__(
        self, *, results: typing.List[ListMarketplaceDDAResponseModel], **kwargs
    ):
        super().__init__(**kwargs)

        # Model attributes
        self.results = results


class ListMarketplaceDDAResponseBodySchema(BaseModelSchema):
    class Meta:
        # model class
        model_class = ListMarketplaceDDAResponseBody

        # Unknown fields are excluded
        unknown = EXCLUDE

    results = fields.List(fields.Nested(ListMarketplaceDDAResponseModelSchema))
