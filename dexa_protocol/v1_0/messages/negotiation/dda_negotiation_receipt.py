from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from marshmallow import EXCLUDE, fields
from ...message_types import PROTOCOL_PACKAGE, NEGOTIATION_RECEIPT
from ...models.dda_negotiation_receipt_model import (
    DDANegotiationReceiptBodyModel,
    DDANegotiationReceiptBodyModelSchema
)

HANDLER_CLASS = (
    f"{PROTOCOL_PACKAGE}.handlers.dda_negotiation_receipt_handler.DDANegotiationReceiptHandler"
)


class DDANegotiationReceiptMessage(AgentMessage):
    """DDA negotiation receipt message"""

    class Meta:
        # Handler class
        handler_class = HANDLER_CLASS

        # Message type
        message_type = NEGOTIATION_RECEIPT

        # Schema class
        schema_class = "DDANegotiationReceiptMessageSchema"

    def __init__(self, *, body: DDANegotiationReceiptBodyModel, **kwargs):
        """Initialise request DDA message"""

        # Initialise the parent class
        super().__init__(**kwargs)

        self.body = body


class DDANegotiationReceiptMessageSchema(AgentMessageSchema):
    """DDA negotiation receipt message schema"""

    class Meta:
        # Model class
        model_class = DDANegotiationReceiptMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    body = fields.Nested(DDANegotiationReceiptBodyModelSchema)
