"""Message type identifiers for Connections."""

from aries_cloudagent.protocols.didcomm_prefix import DIDCommPrefix

SPEC_URI = "https://github.com/decentralised-dataexchange/data-exchange-agreements"

# Message types
BASIC_MESSAGE = f"sample/1.0/message"

# Data market place
PUBLISH_DDA = f"data-marketplace/1.0/publish-dda"
DELETE_DDA = f"data-marketplace/1.0/delete-dda"


PROTOCOL_PACKAGE = "dexa_protocol.v1_0"

MESSAGE_TYPES = DIDCommPrefix.qualify_all(
    {
        BASIC_MESSAGE: f"{PROTOCOL_PACKAGE}.messages.sample_message.SampleMessage",
        PUBLISH_DDA: f"{PROTOCOL_PACKAGE}.messages.publish_dda.PublishDDAMessage",
        DELETE_DDA: f"{PROTOCOL_PACKAGE}.messages.delete_dda.DeleteDDAMessage"
    }
)
