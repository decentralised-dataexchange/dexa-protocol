from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from marshmallow import EXCLUDE, fields
from ...message_types import PROTOCOL_PACKAGE, PUBLISH_DDA
from ...models.publish_dda_model import (
    PublishDDAModel,
    PublishDDAModelSchema
)

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.publish_dda_handler.PublishDDAMessageHandler"


class PublishDDAMessage(AgentMessage):
    """Publish DDA message"""

    class Meta:
        # Handler class
        handler_class = HANDLER_CLASS

        # Message type
        message_type = PUBLISH_DDA

        # Schema class
        schema_class = "PublishDDAMessageSchema"

    def __init__(self, *, body: PublishDDAModel, **kwargs):
        """Initialise publish DDA message"""

        # Initialise the parent class
        super().__init__(**kwargs)

        self.body = body


class PublishDDAMessageSchema(AgentMessageSchema):

    class Meta:
        # Model class
        model_class = PublishDDAMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    body = fields.Nested(PublishDDAModelSchema)
