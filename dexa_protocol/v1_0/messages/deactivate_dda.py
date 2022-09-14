from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from dexa_protocol.v1_0.message_types import DEACTIVATE_DDA, PROTOCOL_PACKAGE
from dexa_protocol.v1_0.models.deactivate_dda_model import (
    DeactivateDDABodyModel,
    DeactivateDDABodyModelSchema,
)
from marshmallow import EXCLUDE, fields

HANDLER_CLASS = (
    f"{PROTOCOL_PACKAGE}.handlers.deactivate_dda_handler.DeactivateDDAMessageHandler"
)


class DeactivateDDAMessage(AgentMessage):
    class Meta:
        handler_class = HANDLER_CLASS
        message_type = DEACTIVATE_DDA
        schema_class = "DeactivateDDAMessageSchema"

    def __init__(self, *, body: DeactivateDDABodyModel, **kwargs):
        super().__init__(**kwargs)

        self.body = body


class DeactivateDDAMessageSchema(AgentMessageSchema):
    class Meta:
        model_class = DeactivateDDAMessage
        unknown = EXCLUDE

    body = fields.Nested(DeactivateDDABodyModelSchema)
