from aries_cloudagent.messaging.models.base import BaseModel, BaseModelSchema
from marshmallow import EXCLUDE, fields


class RequestDDAModel(BaseModel):
    """Request DDA model"""

    class Meta:
        # Schema class
        schema_class = "RequestDDAModelSchema"

    def __init__(self, *, template_id: str, **kwargs):
        """Initialise request DDA model.

        Args:
            template_id (str): Template identifier
        """
        super().__init__(**kwargs)

        # Set model attributes.
        self.template_id = template_id


class RequestDDAModelSchema(BaseModelSchema):
    """Request DDA model schema"""

    class Meta:
        # Model class
        model_class = RequestDDAModel

        # Unknown fields are excluded
        unknown = EXCLUDE

    template_id = fields.Str()
