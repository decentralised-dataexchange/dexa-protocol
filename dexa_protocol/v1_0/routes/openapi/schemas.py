from aries_cloudagent.messaging.models.openapi import OpenAPISchema
from marshmallow import fields


class PersonalDataOpenAPISchema(OpenAPISchema):
    """Personal data open api schema"""

    attribute_name = fields.Str(data_key="attributeName")
    attribute_sensitive = fields.Str(data_key="attributeSensitive", required=False)
    attribute_category = fields.Str(data_key="attributeCategory", required=False)
    attribute_description = fields.Str(data_key="attributeDescription")


class DataSharingRestrictionsOpenAPISchema(OpenAPISchema):
    """Data sharing restrictions open api schema"""

    policy_url = fields.Str(data_key="policyUrl")
    jurisdiction = fields.Str(data_key="jurisdiction")
    industry_sector = fields.Str(data_key="industrySector")
    data_retention_period = fields.Int(data_key="dataRetentionPeriod")
    geographic_restriction = fields.Str(data_key="geographicRestriction")
    storage_location = fields.Str(data_key="storageLocation")


class DataControllerOpenAPISchema(OpenAPISchema):
    """Data controller open api schema"""

    name = fields.Str(data_key="name")
    legal_id = fields.Str(data_key="legalId")
    url = fields.Str(data_key="url")
    industry_sector = fields.Str(data_key="industrySector")


class CreateDataDisclosureAgreementTemplateRequestSchema(OpenAPISchema):
    """Create data disclosure agreement template request schema"""

    language = fields.Str(data_key="language")
    data_controller = fields.Nested(
        DataControllerOpenAPISchema, data_key="dataController"
    )
    agreement_period = fields.Int(data_key="agreementPeriod")
    data_sharing_restrictions = fields.Nested(
        DataSharingRestrictionsOpenAPISchema, data_key="dataSharingRestrictions"
    )
    purpose = fields.Str(data_key="purpose")
    purpose_description = fields.Str(data_key="purposeDescription")
    lawful_basis = fields.Str(data_key="lawfulBasis")
    personal_data = fields.List(
        fields.Nested(PersonalDataOpenAPISchema), data_key="personalData"
    )
    code_of_conduct = fields.Str(data_key="codeOfConduct")


class CreateDDATemplateRequestQueryStringSchema(OpenAPISchema):
    """Create dda template query string schema"""

    publish_flag = fields.Boolean()
    da_template_id = fields.Str()


class QueryDDATemplateQueryStringSchema(OpenAPISchema):
    """Query dda template query string schema."""

    template_id = fields.Str(required=False)
    template_version = fields.Str(required=False)
    industry_sector = fields.Str(required=False)
    publish_flag = fields.Bool(required=False)
    delete_flag = fields.Bool(required=False)
    latest_version_flag = fields.Bool(required=False)
    page = fields.Int(required=False)
    page_size = fields.Int(required=False)


class UpdateDDATemplateQueryStringSchema(OpenAPISchema):
    """Update DDA template query string."""

    publish_flag = fields.Boolean(required=True)


class UpdateDDATemplateRequestSchema(OpenAPISchema):
    """Create DDA template request schema"""

    language = fields.Str(data_key="language")
    data_controller = fields.Nested(
        DataControllerOpenAPISchema, data_key="dataController"
    )
    agreement_period = fields.Int(data_key="agreementPeriod")
    data_sharing_restrictions = fields.Nested(
        DataSharingRestrictionsOpenAPISchema, data_key="dataSharingRestrictions"
    )
    purpose = fields.Str(data_key="purpose")
    purpose_description = fields.Str(data_key="purposeDescription")
    lawful_basis = fields.Str(data_key="lawfulBasis")
    personal_data = fields.List(
        fields.Nested(PersonalDataOpenAPISchema), data_key="personalData"
    )
    code_of_conduct = fields.Str(data_key="codeOfConduct")


class DDATemplateMatchInfoSchema(OpenAPISchema):
    """DDA template match info schema"""

    template_id = fields.Str()


class AddMarketPlaceConnectionMatchInfoSchema(OpenAPISchema):
    """Mark connection as marketplace match info schema"""

    connection_id = fields.Str()


class QueryMarketplaceConnectionsQueryInfoSchema(OpenAPISchema):
    """Query marketplace connections query info schema"""

    connection_id = fields.Str()


class PublishDDAToMarketplaceMatchInfoSchema(OpenAPISchema):
    """Publish DDa to marketplace match info schema"""

    template_id = fields.Str()
    connection_id = fields.Str()


class QueryPublishedDDATemplatesQueryString(OpenAPISchema):
    """Query published DDA templates query string schema"""

    page = fields.Int(required=False)
    page_size = fields.Int(required=False)


class ListDDAPublishedInMarketplaceQueryStringSchema(OpenAPISchema):
    """List DDA published in marketplace query string schema"""

    page = fields.Int(required=False)
    page_size = fields.Int(required=False)


class QueryPublishedDDATemplatesForMarketplaceConnectionMatchInfoSchema(OpenAPISchema):
    """Query published DDA templates for marketplace connection match info schema"""

    connection_id = fields.Str()


class RequestDDAFromDataSourceMatchInfoSchema(OpenAPISchema):
    """Request DDA from Data Source match info schema"""

    connection_id = fields.Str()
    template_id = fields.Str()


class QueryDDAInstancesQueryStringSchema(OpenAPISchema):
    """
    Query DDA instances
    """

    instance_id = fields.Str(required=False)
    template_id = fields.Str(required=False)
    template_version = fields.Str(required=False)
    connection_id = fields.Str(required=False)
    page = fields.Int(required=False)
    page_size = fields.Int(required=False)


class DeactivateDDAMatchInfoSchema(OpenAPISchema):
    """Deactivate DDA match info schema"""

    instance_id = fields.Str()


class SendPullDataRequestMatchInfo(OpenAPISchema):
    """Send pull data request match info"""

    instance_id = fields.Str()


class QueryPullDataRecordsQueryStringSchema(OpenAPISchema):
    """
    Query pull data records query string schema.
    """

    dda_instance_id = fields.Str(required=False)
    dda_template_id = fields.Str(required=False)
    page = fields.Int(required=False)
    page_size = fields.Int(required=False)
