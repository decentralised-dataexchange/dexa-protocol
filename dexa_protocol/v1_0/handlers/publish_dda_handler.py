from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)
from dexa_protocol.v1_0.messages.marketplace.publish_dda import PublishDDAMessage
from dexa_sdk.managers.dexa_manager import DexaManager


class PublishDDAMessageHandler(BaseHandler):
    """Publish DDA message handler logic"""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Handle function"""

        assert isinstance(context.message, PublishDDAMessage)

        # Initialise the manager
        mgr = DexaManager(context)

        # Process publish dda request message.
        await mgr.process_publish_dda_request_message(
            context.message, context.message_receipt
        )
