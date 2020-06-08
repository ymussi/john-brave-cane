from flask_restplus import Resource
from flask_accepts import accepts
from brave_cane.api import api
from brave_cane.api.partner import schemas

import requests
import logging

log = logging.getLogger(__name__)
ns = api.namespace('partner', description='')


@ns.route('/')
class RegisterPartner(Resource):
    @accepts(schema=schemas.Partner, api=api)
    def post(self):
        """
        Perform a registration for new partner.
        """

        data = requests.json
        response = data

        return response

@ns.route('/<string:id>')
class GetPartnerByID(Resource):
    @accepts(schema=schemas.Partner, api=api)
    def get(self, id):
        """
        Get a specific partner by id
        """

        response = id

        return response.json

@ns.route('/<string:lng>/<string:lat>')
class GetPartnerByCoordinates(Resource):
    def get(self, lng, lat):
        """
        Search the nearest partner with a specific location (coordinates lng and lat).
        """

        response = {'lng': lng, 'lat': lat}

        return response
