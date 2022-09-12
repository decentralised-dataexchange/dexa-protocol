from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from marshmallow import EXCLUDE, fields
from ...message_types import PROTOCOL_PACKAGE, REQUEST_DDA
from ...models.request_dda_model import RequestDDAModel, RequestDDAModelSchema

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.request_dda_handler.RequestDDAMessageHandler"


class RequestDDAMessage(AgentMessage):
    """Request DDA message"""

    class Meta:
        # Handler class
        handler_class = HANDLER_CLASS

        # Message type
        message_type = REQUEST_DDA

        # Schema class
        schema_class = "RequestDDAMessageSchema"

    def __init__(self, *, body: RequestDDAModel, **kwargs):
        """Initialise request DDA message"""

        # Initialise the parent class
        super().__init__(**kwargs)

        self.body = body


class RequestDDAMessageSchema(AgentMessageSchema):
    """Request DDA message schema"""

    class Meta:
        # Model class
        model_class = RequestDDAMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    body = fields.Nested(RequestDDAModelSchema)
