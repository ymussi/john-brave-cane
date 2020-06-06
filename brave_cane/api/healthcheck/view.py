from flask_restplus import Resource
from brave_cane.api import api

import logging

log = logging.getLogger(__name__)
ns = api.namespace('healthcheck', description='')

@ns.route('/')
class HealhCheck(Resource):
    @ns.response(code=400, description='Bad Request')
    def get(self):
        """
        Healhcheck endpoint.
        """

        return {'status': True, 'message': 'All Fine.'}