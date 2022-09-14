"""Basic message handler."""
import json

from aries_cloudagent.messaging.base_handler import (
    BaseHandler,
    BaseResponder,
    RequestContext,
)
from dexa_protocol.v1_0.messages.marketplace.list_marketplace_dda import (
    ListMarketplaceDDAMessage,
)
from dexa_sdk.managers.dexa_manager import DexaManager
from loguru import logger


class ListMarketplaceDDAMessageHandler(BaseHandler):
    """Message handler class for list marketplace dda message."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Handle function.

        Args:
            context: request context
            responder: responder callback
        """

        assert isinstance(context.message, ListMarketplaceDDAMessage)

        logger.info(
            f"Received message: {json.dumps(context.message.serialize(), indent=4)}"
        )

        # Initialise the manager
        mgr = DexaManager(context)

        # Process the message
        await mgr.process_list_marketplace_dda_message(
            context.message, context.message_receipt
        )
