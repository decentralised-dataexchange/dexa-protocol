from aiohttp import web
from dexa_protocol.v1_0.routes.dda_routes import (
    create_data_disclosure_agreement_handler,
    deactivate_dda_instance_handler,
    delete_dda_template_handler,
    list_dda_published_in_marketplace,
    publish_dda_template_handler,
    publish_dda_to_marketplace_handler,
    query_dda_handler,
    query_dda_instances_handler,
    request_dda_offer_from_ds_handler,
    update_dda_template_handler,
)
from dexa_protocol.v1_0.routes.marketplace_routes import (
    add_marketplace_connection_handler,
    query_marketplace_connections_handler,
    query_publish_dda_template_for_marketplace_connection,
    query_published_dda_template_handler,
)

# Data Disclosure Agreement routes
ROUTES_DDA = [
    web.post(
        "/v1/data-disclosure-agreements",
        create_data_disclosure_agreement_handler,
    ),
    web.get("/v1/data-disclosure-agreements", query_dda_handler, allow_head=False),
    web.post(
        "/v1/data-disclosure-agreements/{template_id}", update_dda_template_handler
    ),
    web.delete(
        "/v1/data-disclosure-agreements/{template_id}", delete_dda_template_handler
    ),
    web.post(
        "/v1/data-disclosure-agreements/{template_id}/publish",
        publish_dda_template_handler,
    ),
    web.post(
        "/v1/data-disclosure-agreements/{template_id}/marketplace/{connection_id}",
        publish_dda_to_marketplace_handler,
    ),
    web.get(
        "/v1/data-disclosure-agreements/marketplace",
        list_dda_published_in_marketplace,
        allow_head=False,
    ),
    web.post(
        "/v1/data-disclosure-agreements/{template_id}/request/connections/{connection_id}",
        request_dda_offer_from_ds_handler,
    ),
    web.get(
        "/v1/auditor/data-disclosure-agreements/instances",
        query_dda_instances_handler,
        allow_head=False,
    ),
    web.post(
        "/v1/data-disclosure-agreements/instances/{instance_id}/deactivate",
        deactivate_dda_instance_handler,
    ),
]


MARKETPLACE_ROUTES = [
    web.post(
        "/v1/data-marketplace/connections/{connection_id}",
        add_marketplace_connection_handler,
    ),
    web.get(
        "/v1/data-marketplace/connections",
        query_marketplace_connections_handler,
        allow_head=False,
    ),
    web.get(
        "/v1/data-marketplace/published-dda",
        query_published_dda_template_handler,
        allow_head=False,
    ),
    web.get(
        "/v1/data-marketplace/{connection_id}/published-dda",
        query_publish_dda_template_for_marketplace_connection,
        allow_head=False,
    ),
]
