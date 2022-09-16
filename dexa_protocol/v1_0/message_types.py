# flake8: noqa
"""Message type identifiers for Connections."""

from aries_cloudagent.protocols.didcomm_prefix import DIDCommPrefix

SPEC_URI = "https://github.com/decentralised-dataexchange/data-exchange-agreements"


# Data market place
PUBLISH_DDA = f"data-marketplace/1.0/publish-dda"
DELETE_DDA = f"data-marketplace/1.0/delete-dda"
LIST_MARKETPLACE_DDA = f"data-marketplace/1.0/list-dda"
LIST_MARKETPLACE_DDA_RESPONSE = f"data-marketplace/1.0/list-dda-response"

# Data Using Service
REQUEST_DDA = f"dda-negotiation/1.0/request-dda"
OFFER_DDA = f"dda-negotiation/1.0/offer-dda"
ACCEPT_DDA = f"dda-negotiation/1.0/accept-dda"
NEGOTIATION_RECEIPT = f"dda-negotiation/1.0/receipt"
DEACTIVATE_DDA = f"dda/1.0/deactivate"

PULLDATA_REQUEST = f"pull-data/1.0/request"
PULLDATA_RESPONSE = f"pull-data/1.0/response"
PULLDATA_NOTIFICATION = f"pull-data/1.0/notification"

PROTOCOL_PACKAGE = "dexa_protocol.v1_0"

MESSAGE_TYPES = DIDCommPrefix.qualify_all(
    {
        PUBLISH_DDA: f"{PROTOCOL_PACKAGE}.messages.marketplace.publish_dda.PublishDDAMessage",
        DELETE_DDA: f"{PROTOCOL_PACKAGE}.messages.marketplace.delete_dda.DeleteDDAMessage",
        LIST_MARKETPLACE_DDA: (
            f"{PROTOCOL_PACKAGE}.messages.marketplace.list_marketplace_dda.ListMarketplaceDDAMessage"
        ),
        REQUEST_DDA: f"{PROTOCOL_PACKAGE}.messages.negotiation.request_dda.RequestDDAMessage",
        OFFER_DDA: f"{PROTOCOL_PACKAGE}.messages.negotiation.offer_dda.OfferDDAMessage",
        ACCEPT_DDA: f"{PROTOCOL_PACKAGE}.messages.negotiation.accept_dda.AcceptDDAMessage",
        NEGOTIATION_RECEIPT: f"{PROTOCOL_PACKAGE}.messages.negotiation.dda_negotiation_receipt.DDANegotiationReceiptMessage",
        DEACTIVATE_DDA: f"{PROTOCOL_PACKAGE}.messages.deactivate_dda.DeactivateDDAMessage",
        PULLDATA_REQUEST: f"{PROTOCOL_PACKAGE}.messages.pulldata_request_message.PullDataRequestMessage",
        PULLDATA_RESPONSE: f"{PROTOCOL_PACKAGE}.messages.pulldata_response_message.PullDataResponseMessage",
    }
)
