from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext
)
from dexa_sdk.managers.dexa_manager import DexaManager
from ..messages.marketplace.delete_dda import DeleteDDAMessage


class DeleteDDAMessageHandler(BaseHandler):
    """Delete DDA message handler logic"""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Handle function"""

        assert isinstance(context.message, DeleteDDAMessage)

        # Initialise the manager
        mgr = DexaManager(context)

        # Process publish dda request message.
        await mgr.process_delete_dda_message(
            context.message,
            context.message_receipt
        )
