from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from marshmallow import EXCLUDE, fields
from ...message_types import PROTOCOL_PACKAGE, ACCEPT_DDA
from ...models.accept_dda_model import (
    AcceptDDAMessageBodyModel,
    AcceptDDAMessageBodyModelSchema
)
HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.accept_dda_handler.AcceptDDAMessageHandler"


class AcceptDDAMessage(AgentMessage):
    """Accept DDA message"""

    class Meta:
        # Handler class
        handler_class = HANDLER_CLASS

        # Message type
        message_type = ACCEPT_DDA

        # Schema class
        schema_class = "AcceptDDAMessageSchema"

    def __init__(self, *, body: AcceptDDAMessageBodyModel, **kwargs):
        """Initialise request DDA message"""

        # Initialise the parent class
        super().__init__(**kwargs)

        self.body = body


class AcceptDDAMessageSchema(AgentMessageSchema):
    """Accept DDA message schema"""

    class Meta:
        # Model class
        model_class = AcceptDDAMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    body = fields.Nested(AcceptDDAMessageBodyModelSchema)
