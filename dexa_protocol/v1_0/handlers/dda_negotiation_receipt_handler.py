from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)
from dexa_protocol.v1_0.messages.negotiation.dda_negotiation_receipt import (
    DDANegotiationReceiptMessage,
)
from dexa_sdk.managers.dexa_manager import DexaManager


class DDANegotiationReceiptHandler(BaseHandler):
    """DDA negotiation receipt message handler logic"""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Handle function"""

        assert isinstance(context.message, DDANegotiationReceiptMessage)

        # Initialise the manager
        mgr = DexaManager(context)

        # Process dda negotiation receipt message.
        await mgr.process_dda_negotiation_receipt_message(
            context.message, context.message_receipt
        )
