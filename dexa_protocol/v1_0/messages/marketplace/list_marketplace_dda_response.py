from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from dexa_protocol.v1_0.message_types import (
    LIST_MARKETPLACE_DDA_RESPONSE,
    PROTOCOL_PACKAGE,
)
from dexa_protocol.v1_0.models.list_marketplace_dda_response_model import (
    ListMarketplaceDDAResponseBody,
    ListMarketplaceDDAResponseBodySchema,
)
from marshmallow import EXCLUDE, fields

HANDLER_CLASS = (
    f"{PROTOCOL_PACKAGE}.handlers.list_marketplace_dda_response_handler"
    f".ListMarketplaceDDAResponseMessageHandler"
)


class ListMarketplaceDDAResponseMessage(AgentMessage):
    """List marketplace DDA response message"""

    class Meta:
        # Handler class
        handler_class = HANDLER_CLASS

        # Message type
        message_type = LIST_MARKETPLACE_DDA_RESPONSE

        # Schema class
        schema_class = "ListMarketplaceDDAResponseMessageSchema"

    def __init__(self, body: ListMarketplaceDDAResponseBody, **kwargs):
        """Initialise the message"""

        # Initialise the parent class
        super().__init__(**kwargs)

        # Set attributes.
        self.body = body


class ListMarketplaceDDAResponseMessageSchema(AgentMessageSchema):
    class Meta:
        # Model class
        model_class = ListMarketplaceDDAResponseMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    body = fields.Nested(ListMarketplaceDDAResponseBodySchema)
