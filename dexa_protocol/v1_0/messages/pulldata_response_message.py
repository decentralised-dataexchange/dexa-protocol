from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from dexa_protocol.v1_0.message_types import PROTOCOL_PACKAGE, PULLDATA_RESPONSE
from marshmallow import EXCLUDE, fields

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.pulldata_response_handler.PullDataResponseMessageHandler"


class PullDataResponseMessage(AgentMessage):
    class Meta:
        handler_class = HANDLER_CLASS
        message_type = PULLDATA_RESPONSE
        schema_class = "PullDataResponseMessageSchema"

    def __init__(self, *, ds_eth_address: str = None, nonce: str = None, **kwargs):
        super().__init__(**kwargs)

        self.ds_eth_address = ds_eth_address
        self.nonce = nonce


class PullDataResponseMessageSchema(AgentMessageSchema):
    class Meta:
        model_class = PullDataResponseMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    ds_eth_address = fields.Str(required=False)
    nonce = fields.Str(required=False)
