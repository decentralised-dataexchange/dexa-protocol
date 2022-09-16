from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from dexa_protocol.v1_0.message_types import PROTOCOL_PACKAGE, PULLDATA_REQUEST
from marshmallow import EXCLUDE, fields

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.pulldata_request_handler.PullDataRequestMessageHandler"


class PullDataRequestMessage(AgentMessage):
    class Meta:
        handler_class = HANDLER_CLASS
        message_type = PULLDATA_REQUEST
        schema_class = "PullDataRequestMessageSchema"

    def __init__(self, *, dda_instance_id: str = None, nonce: str = None, **kwargs):
        super().__init__(**kwargs)

        self.dda_instance_id = dda_instance_id
        self.nonce = nonce


class PullDataRequestMessageSchema(AgentMessageSchema):
    class Meta:
        model_class = PullDataRequestMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    dda_instance_id = fields.Str(required=False)
    nonce = fields.Str(required=False)
