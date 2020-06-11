from brave_cane.api import api
from brave_cane.api.healthcheck import get_first_partner
from flask_restplus import Resource

import logging

log = logging.getLogger(__name__)
ns = api.namespace('healthcheck', description='Communication test.')

@ns.route('/')
class HealhCheck(Resource):
    @ns.response(code=400, description='Bad Request')
    def get(self):
        """
        Healhcheck endpoint.
        """
        resp = get_first_partner()

        return resp