from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from dexa_protocol.v1_0.message_types import LIST_MARKETPLACE_DDA, PROTOCOL_PACKAGE
from marshmallow import EXCLUDE

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.list_marketplace_dda_handler.ListMarketplaceDDAMessageHandler"


class ListMarketplaceDDAMessage(AgentMessage):
    """List marketplace DDA message"""

    class Meta:
        # Handler class
        handler_class = HANDLER_CLASS

        # Message type
        message_type = LIST_MARKETPLACE_DDA

        # Schema class
        schema_class = "ListMarketplaceDDAMessageSchema"

    def __init__(self, **kwargs):
        """Initialise list marketplace DDA message"""

        # Initialise the parent class
        super().__init__(**kwargs)


class ListMarketplaceDDAMessageSchema(AgentMessageSchema):
    class Meta:
        # Model class
        model_class = ListMarketplaceDDAMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE
