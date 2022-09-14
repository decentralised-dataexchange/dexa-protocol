from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from dexa_sdk.agreements.dda.v1_0.models.dda_instance_models import (
    DataDisclosureAgreementInstanceModel,
    DataDisclosureAgreementInstanceSchema,
)
from marshmallow import EXCLUDE, fields


class CustomerIdentificationModel(BaseModel):
    """Customer identification model"""

    class Meta:
        # Schema class
        schema_class = "CustomerIdentificationModelSchema"

    def __init__(self, *, schema_id: str, cred_def_id: str, **kwargs):
        super().__init__(**kwargs)

        # Model attributes.
        self.schema_id = schema_id
        self.cred_def_id = cred_def_id


class CustomerIdentificationModelSchema(BaseModelSchema):
    """Customer identification model schema"""

    class Meta:
        # Model class
        model_class = CustomerIdentificationModel

        # Unknown fields are excluded.
        unknown = EXCLUDE

    # Schema ID
    schema_id = fields.Str()

    # Credential definition ID
    cred_def_id = fields.Str()


class OfferDDAMessageBodyModel(BaseModel):
    """Offer DDA body model"""

    class Meta:
        # Schema class
        schema_class = "OfferDDAMessageBodyModelSchema"

    def __init__(
        self,
        *,
        dda: DataDisclosureAgreementInstanceModel,
        customer_identification: CustomerIdentificationModel = None,
        **kwargs
    ):
        """Initialise offer DDA message body model.

        Args:
            template_id (str): Template identifier
        """
        super().__init__(**kwargs)

        # Set model attributes.
        self.dda = dda
        self.customer_identification = customer_identification


class OfferDDAMessageBodyModelSchema(BaseModelSchema):
    """Offer DDA message body model schema"""

    class Meta:
        # Model class
        model_class = OfferDDAMessageBodyModel

        # Unknown fields are excluded
        unknown = EXCLUDE

    # Signed DDA.
    dda = fields.Nested(DataDisclosureAgreementInstanceSchema)

    # Customer identification data.
    customer_identification = fields.Nested(
        CustomerIdentificationModelSchema, required=False
    )
