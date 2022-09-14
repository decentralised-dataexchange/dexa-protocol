from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)
from dexa_protocol.v1_0.messages.deactivate_dda import DeactivateDDAMessage
from dexa_sdk.managers.dexa_manager import DexaManager


class DeactivateDDAMessageHandler(BaseHandler):
    """Deactivate DDA message handler logic"""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Handle function"""

        assert isinstance(context.message, DeactivateDDAMessage)

        # Initialise the manager.
        mgr = DexaManager(context)

        # Process the message.
        await mgr.process_deactivate_dda_message(
            context.message, context.message_receipt
        )
