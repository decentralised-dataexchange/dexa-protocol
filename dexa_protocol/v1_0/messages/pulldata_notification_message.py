from aries_cloudagent.messaging.agent_message import AgentMessage, AgentMessageSchema
from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from dexa_protocol.v1_0.message_types import PROTOCOL_PACKAGE, PULLDATA_NOTIFICATION
from marshmallow import EXCLUDE, fields

HANDLER_CLASS = f"{PROTOCOL_PACKAGE}.handlers.pulldata_notification_handler.PullDataNotificationMessageHandler"


class PDNControllerDetailsModel(BaseModel):
    class Meta:
        schema_class = "PDNControllerDetailsModelSchema"

    def __init__(
        self,
        organisation_did: str = None,
        organisation_name: str = None,
        cover_image_url: str = None,
        logo_image_url: str = None,
        location: str = None,
        organisation_type: str = None,
        description: str = None,
        policy_url: str = None,
        eula_url: str = None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.organisation_did = organisation_did
        self.organisation_name = organisation_name
        self.cover_image_url = cover_image_url
        self.logo_image_url = logo_image_url
        self.location = location
        self.organisation_type = organisation_type
        self.description = description
        self.policy_url = policy_url
        self.eula_url = eula_url


class PDNControllerDetailsModelSchema(BaseModelSchema):
    class Meta:
        model_class = PDNControllerDetailsModel
        unknown = EXCLUDE

    organisation_did = fields.Str(required=False)
    organisation_name = fields.Str(required=False)
    cover_image_url = fields.Str(required=False)
    logo_image_url = fields.Str(required=False)
    location = fields.Str(required=False)
    organisation_type = fields.Str(required=False)
    description = fields.Str(required=False)
    policy_url = fields.Str(required=False)
    eula_url = fields.Str(required=False)


class PullDataNotificationMessage(AgentMessage):
    class Meta:
        handler_class = HANDLER_CLASS
        message_type = PULLDATA_NOTIFICATION
        schema_class = "PullDataNotificationMessageSchema"

    def __init__(
        self,
        *,
        da_instance_id: str = None,
        controller_details: PDNControllerDetailsModel = None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.da_instance_id = da_instance_id
        self.controller_details = controller_details


class PullDataNotificationMessageSchema(AgentMessageSchema):
    class Meta:
        model_class = PullDataNotificationMessage

        # Unknown fields are excluded.
        unknown = EXCLUDE

    da_instance_id = fields.Str(required=False)
    controller_details = fields.Nested(PDNControllerDetailsModelSchema, required=False)
