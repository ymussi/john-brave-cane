from brave_cane.database.models import PDV
from werkzeug.exceptions import BadRequest, UnprocessableEntity


class PartnerValidations:
    
    def payload_validations(self, pdv):    
        coverageArea = pdv.get('coverageArea').get('coordinates')
        address = pdv.get('address').get('coordinates')
        id_exists = PDV.get(id=(pdv.get('id')))
        
        if pdv.get('id') == 0:
            raise BadRequest('Please fill in all the information to register your partner.') 
        
        if id_exists:
            raise BadRequest(f"The pdv '{pdv['tradingName']}' couldn't be registered. Motive: id '{pdv['id']}' already exists.")
                    
        if len(address) < 2:
            raise UnprocessableEntity(
                    "A partner Address list must have at least 2 coordinate parameters like this example: [-23.58, -46.67].")
            
        for k in pdv:
            if k in('ownerName', 'document', 'tradingName'):
                if pdv[k] == 'string':
                    raise BadRequest(f"Please fill in the field '{k}'")
            if k in ('address', 'coverageArea'):
                if pdv[k].get('type') not in ('MultiPolygon', 'Point'):
                    raise BadRequest(f"Please fill in the field '{k}': 'type' must be 'MultiPolygon' or 'Point'")
        
        for polygon in coverageArea:
            if len(polygon[0]) < 3:
                raise UnprocessableEntity(
                    "A partner's CoverageArea must have at least 3 lists of coordinates like this example: [[[[-23.58, -46.67], [-23.58, -46.67], [-23.58, -46.67]]]]")
            
            for point in polygon[0]:
                if len(point) < 2:
                    raise UnprocessableEntity(
                        "A partner' CoverageArea coordinate list must have at least 2 coordinate parameters like this example: [[[[-23.58, -46.67], [-23.58, -46.67], [-23.58, -46.67]]]].")
        
        return True