from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from dexa_sdk.agreements.dda.v1_0.models.dda_instance_models import (
    DataDisclosureAgreementInstanceModel,
    DataDisclosureAgreementInstanceSchema,
)
from marshmallow import EXCLUDE, fields


class AcceptDDAMessageBodyModel(BaseModel):
    """Accept DDA body model"""

    class Meta:
        # Schema class
        schema_class = "AcceptDDAMessageBodyModelSchema"

    def __init__(self, *, dda: DataDisclosureAgreementInstanceModel, **kwargs):
        """Initialise accept DDA message body model.

        Args:
            template_id (str): Template identifier
        """
        super().__init__(**kwargs)

        # Set model attributes.
        self.dda = dda


class AcceptDDAMessageBodyModelSchema(BaseModelSchema):
    """Accept DDA message body model schema"""

    class Meta:
        # Model class
        model_class = AcceptDDAMessageBodyModel

        # Unknown fields are excluded
        unknown = EXCLUDE

    # Signed DDA.
    dda = fields.Nested(DataDisclosureAgreementInstanceSchema)
