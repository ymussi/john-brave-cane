from brave_cane.api import api
from brave_cane.api.partner import schemas
from brave_cane.api.partner.controller import PartnerManager
from flask_restplus import Resource
from flask import request
from flask_accepts import accepts

import logging

log = logging.getLogger(__name__)
ns = api.namespace('partner', description='Registration and partner search.')


@ns.route('/')
class RegisterPartner(Resource):
    @accepts(schema=schemas.Pdvs, api=api)
    def post(self):
        """
        Perform a registration for new partner.
        """
        pdvs = request.json
        pdv = PartnerManager().save(pdvs)
        return pdv


@ns.route('/<string:id>')
class GetPartnerByID(Resource):
    def get(self, id):
        """
        Get a specific partner by id
        """
        pdv = PartnerManager().get_by_id(id)
        return pdv


@ns.route('/<string:lat>/<string:lng>')
class GetPartnerByCoordinates(Resource):
    def get(self, lat, lng):
        """
        Search the nearest partner with a specific location 
        (coordinates lng and lat).
        """
        nearest_partner = PartnerManager().get_by_coordinates(lat, lng)
        return nearest_partner
