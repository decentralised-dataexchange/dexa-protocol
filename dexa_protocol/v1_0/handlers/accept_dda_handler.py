from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext
)
from dexa_sdk.managers.dexa_manager import DexaManager
from ..messages.negotiation.accept_dda import AcceptDDAMessage


class AcceptDDAMessageHandler(BaseHandler):
    """Accept DDA message handler logic"""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Handle function"""

        assert isinstance(context.message, AcceptDDAMessage)

        # Initialise the manager.
        mgr = DexaManager(context)

        # Process the message.
        await mgr.process_accept_dda_message(
            context.message,
            context.message_receipt
        )
