"""Message type identifiers for Connections."""

from aries_cloudagent.protocols.didcomm_prefix import DIDCommPrefix

SPEC_URI = "https://github.com/decentralised-dataexchange/data-exchange-agreements"

# Message types
BASIC_MESSAGE = f"sample/1.0/message"

PROTOCOL_PACKAGE = "dexa_sdk.plugin.v1_0"

MESSAGE_TYPES = DIDCommPrefix.qualify_all(
    {BASIC_MESSAGE: f"{PROTOCOL_PACKAGE}.messages.sample_message.SampleMessage"}
)
