from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)
from dexa_protocol.v1_0.messages.pulldata_response_message import (
    PullDataResponseMessage,
)
from dexa_sdk.managers.dexa_manager import DexaManager


class PullDataResponseMessageHandler(BaseHandler):
    async def handle(self, context: RequestContext, responder: BaseResponder):

        assert isinstance(context.message, PullDataResponseMessage)

        # Initialise the manager
        mgr = DexaManager(context)

        # Process message.
        await mgr.process_pull_data_response_message(
            context.message, context.message_receipt
        )
