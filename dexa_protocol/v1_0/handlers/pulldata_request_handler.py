from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)
from dexa_protocol.v1_0.messages.pulldata_request_message import PullDataRequestMessage
from dexa_sdk.managers.dexa_manager import DexaManager


class PullDataRequestMessageHandler(BaseHandler):
    async def handle(self, context: RequestContext, responder: BaseResponder):

        assert isinstance(context.message, PullDataRequestMessage)

        # Initialise the manager
        mgr = DexaManager(context)

        # Process message.
        await mgr.process_pulldata_request_message(
            context.message, context.message_receipt
        )
