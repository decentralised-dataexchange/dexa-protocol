from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from marshmallow import EXCLUDE, fields
from ...message_types import PROTOCOL_PACKAGE, DELETE_DDA
from ...models.delete_dda_model import (
    DeleteDDAModel,
    DeleteDDAModelSchema
)

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.delete_dda_handler.DeleteDDAMessageHandler"


class DeleteDDAMessage(AgentMessage):
    """Delete DDA message"""

    class Meta:
        # Handler class
        handler_class = HANDLER_CLASS

        # Message type
        message_type = DELETE_DDA

        # Schema class
        schema_class = "DeleteDDAMessageSchema"

    def __init__(self, *, body: DeleteDDAModel, **kwargs):
        """Initialise delete DDA message"""

        # Initialise the parent class
        super().__init__(**kwargs)

        self.body = body


class DeleteDDAMessageSchema(AgentMessageSchema):
    """Delete DDA message schema"""

    class Meta:
        # Model class
        model_class = DeleteDDAMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    body = fields.Nested(DeleteDDAModelSchema)
