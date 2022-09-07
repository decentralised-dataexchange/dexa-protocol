from aiohttp import web
from ..dda_routes import (
    create_data_disclosure_agreement_handler,
    query_dda_handler,
    update_dda_template_handler,
    delete_dda_template_handler,
    publish_dda_template_handler
)

# Data Disclosure Agreement routes
ROUTES_DDA = [
    web.post(
        "/v1/data-disclosure-agreements",
        create_data_disclosure_agreement_handler,
    ),
    web.get(
        "/v1/data-disclosure-agreements",
        query_dda_handler,
        allow_head=False
    ),
    web.post(
        "/v1/data-disclosure-agreements/{template_id}",
        update_dda_template_handler
    ),
    web.delete(
        "/v1/data-disclosure-agreements/{template_id}",
        delete_dda_template_handler
    ),
    web.post(
        "/v1/data-disclosure-agreements/{template_id}/publish",
        publish_dda_template_handler
    ),
]
