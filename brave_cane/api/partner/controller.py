from brave_cane.api.partner.service import PartnerServices
from brave_cane.database.models import PDV
from brave_cane.database import session
from brave_cane.conector.mysql import CadastroDBContext
from werkzeug.exceptions import BadRequest, UnprocessableEntity
import logging

class PartnerManager:
    
    def save(self, pdvs):
        for pdv in pdvs['pdvs']:
            coverageArea = pdv['coverageArea']['coordinates']
            address = pdv['address']['coordinates']
            id_exists = PDV.get(id=(pdv['id']))
            
            if pdv['id'] == 0:
                raise BadRequest('Please fill in all the information to register your partner.') 
            
            if id_exists:
                raise BadRequest(f"The pdv '{pdv['tradingName']}' couldn't be registered. Motive: id '{pdv['id']}' already exists.")
                        
            if len(address) < 2:
                raise UnprocessableEntity(
                        "A partner Address list must have at least 2 coordinate parameters like this example: [-23.58, -46.67].")
            
            for polygon in coverageArea:
                if len(polygon[0]) < 3:
                    raise UnprocessableEntity(
                        "A partner's CoverageArea must have at least 3 lists of coordinates like this example: [[[[-23.58, -46.67], [-23.58, -46.67], [-23.58, -46.67]]]]")
              
                if len(polygon[0][0]) < 2:
                    raise UnprocessableEntity(
                        "A partner coordinate list must have at least 2 coordinate parameters like this example: [[[[-23.58, -46.67], [-23.58, -46.67], [-23.58, -46.67]]]].")
                
            obj = PDV(**pdv)
            session.add(obj)
        try:
            logging.info(f'Data recorded in the database: {pdv}')
            session.commit()    
            return {"status": True, "msg": "All pdvs have been registered."}
        except Exception as e:
            session.rollback()
            session.close()
            raise BadRequest(f"The pdvs couldn't be registered. - err: {str(e)}")

    def get_by_id(self, id):
        obj = PDV.get(id=id)
        if obj:
            return obj.as_dict()
        else:
            raise BadRequest("Partner not found or not registered.")

    def get_by_coordinates(self, lat, lng):
        objs = PDV.get_all()
        pdvs = []
        for obj in objs:
            pdv = {"id": obj.id,
                   "coverageArea": obj.coverageArea,
                   "address": obj.address}
            pdvs.append(pdv)
        
        client_coordinates = {"lat": float(lat),  "lng": float(lng)}
        pdv = PartnerServices().get_nearest_partner(pdvs, client_coordinates)

        return pdv
