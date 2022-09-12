from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from marshmallow import EXCLUDE, fields
from ...message_types import PROTOCOL_PACKAGE, OFFER_DDA
from ...models.offer_dda_model import (
    OfferDDAMessageBodyModel,
    OfferDDAMessageBodyModelSchema
)

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.offer_dda_handler.OfferDDAMessageHandler"


class OfferDDAMessage(AgentMessage):
    """Offer DDA message"""

    class Meta:
        # Handler class
        handler_class = HANDLER_CLASS

        # Message type
        message_type = OFFER_DDA

        # Schema class
        schema_class = "OfferDDAMessageSchema"

    def __init__(self, *, body: OfferDDAMessageBodyModel, **kwargs):
        """Initialise request DDA message"""

        # Initialise the parent class
        super().__init__(**kwargs)

        self.body = body


class OfferDDAMessageSchema(AgentMessageSchema):
    """Offer DDA message schema"""

    class Meta:
        # Model class
        model_class = OfferDDAMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    body = fields.Nested(OfferDDAMessageBodyModelSchema)
