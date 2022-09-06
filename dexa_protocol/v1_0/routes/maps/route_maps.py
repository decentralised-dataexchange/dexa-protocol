from aiohttp import web
from ..dda_routes import create_data_disclosure_agreement_handler

# Data Disclosure Agreement routes
ROUTES_DDA = [
    web.post(
        "/v1/data-disclosure-agreements",
        create_data_disclosure_agreement_handler,
    )
]
