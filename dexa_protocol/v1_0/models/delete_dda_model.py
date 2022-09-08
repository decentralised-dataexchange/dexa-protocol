from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from marshmallow import EXCLUDE, fields


class DeleteDDAModel(BaseModel):
    """Delete DDA model"""

    class Meta:
        # Schema class
        schema_class = "DeleteDDAModelSchema"

    def __init__(self, *, template_id: str, **kwargs):
        """Initialise delete DDA model.

        Args:
            template_id (str): Template identifier
        """
        super().__init__(**kwargs)

        # Set model attributes.
        self.template_id = template_id


class DeleteDDAModelSchema(BaseModelSchema):
    """Delete DDA model schema"""

    class Meta:
        # Model class
        model_class = DeleteDDAModel

        # Unknown fields are excluded
        unknown = EXCLUDE

    template_id = fields.Str()
