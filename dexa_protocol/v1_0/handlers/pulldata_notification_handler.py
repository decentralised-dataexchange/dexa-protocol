from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)
from dexa_protocol.v1_0.messages.pulldata_notification_message import (
    PullDataNotificationMessage,
)
from dexa_sdk.managers.dexa_manager import DexaManager


class PullDataNotificationMessageHandler(BaseHandler):
    async def handle(self, context: RequestContext, responder: BaseResponder):

        assert isinstance(context.message, PullDataNotificationMessage)

        # Initialise the manager
        mgr = DexaManager(context)

        # Process message.
        await mgr.process_pulldata_notification_message(
            context.message, context.message_receipt
        )
