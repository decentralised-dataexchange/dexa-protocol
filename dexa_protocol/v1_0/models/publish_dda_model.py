from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from dexa_sdk.agreements.dda.v1_0.models.dda_models import (
    DataDisclosureAgreementModel,
    DataDisclosureAgreementSchema,
)
from marshmallow import EXCLUDE, fields


class PublishDDAModel(BaseModel):
    """Publish DDA model"""

    class Meta:
        # Schema class
        schema_class = "PublishDDAModelSchema"

    def __init__(self, *, dda: DataDisclosureAgreementModel, connection_url: str):

        # Call the parent constructor
        super().__init__()

        # Set model attributes
        self.dda = dda
        self.connection_url = connection_url


class PublishDDAModelSchema(BaseModelSchema):
    """Publish DDA model schema"""

    class Meta:

        # Model class
        model_class = PublishDDAModel

        # Unknown fields are excluded
        unknown = EXCLUDE

    dda = fields.Nested(DataDisclosureAgreementSchema)
    connection_url = fields.Str()
