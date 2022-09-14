from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from marshmallow import EXCLUDE, fields


class DeactivateDDABodyModel(BaseModel):
    class Meta:
        schema_class = "DeactivateDDABodyModelSchema"

    def __init__(self, *, instance_id: str, **kwargs):
        super().__init__(**kwargs)

        self.instance_id = instance_id


class DeactivateDDABodyModelSchema(BaseModelSchema):
    class Meta:
        model_class = DeactivateDDABodyModel
        unknown = EXCLUDE

    instance_id = fields.Str()
