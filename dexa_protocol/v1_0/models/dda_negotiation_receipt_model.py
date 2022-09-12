from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from marshmallow import EXCLUDE, fields


class DDANegotiationReceiptBodyModel(BaseModel):
    """DDA negotiation receipt body model"""

    class Meta:
        # Schema class
        schema_class = "DDANegotiationReceiptBodyModelSchema"

    def __init__(
        self,
        *,
        instance_id: str,
        blockchain_receipt: dict,
        blink: str,
        mydata_did: str,
        **kwargs
    ):
        super().__init__(**kwargs)

        # Set model attributes.
        self.blockchain_receipt = blockchain_receipt
        self.blink = blink
        self.mydata_did = mydata_did
        self.instance_id = instance_id


class DDANegotiationReceiptBodyModelSchema(BaseModelSchema):
    """DDA negotiation receipt message body model schema"""

    class Meta:
        # Model class
        model_class = DDANegotiationReceiptBodyModel

        # Unknown fields are excluded
        unknown = EXCLUDE

    instance_id = fields.Str()
    blockchain_receipt = fields.Dict()
    blink = fields.Str()
    mydata_did = fields.Str()
