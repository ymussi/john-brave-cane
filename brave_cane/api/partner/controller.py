from brave_cane.api.partner.service import PartnerServices
from brave_cane.database.models import PDV
from brave_cane.database import session
from brave_cane.conector.mysql import CadastroDBContext

class PartnerManager:
    
    def save(self, pdvs):
        for pdv in pdvs['pdvs']:
            if pdv['id'] == 0:
                return {"status": True, "msg": "Please fill in all the information to register your partner."}
            pdv = PDV(**pdv)
            session.add(pdv)
        try:
            session.commit()    
            return {"status": True, "msg": "All pdvs have been registered."}
        except Exception as e:
            session.rollback()
            session.close()
            return {"status": False, "msg": "The pdvs couldn't be registered.", "err": str(e)}

    def get_by_id(self, id):
        obj = PDV.get(id=id)
        if obj:
            return obj.as_dict()
        else:
            return {"status": False, "msg": "Partner not found or not registered."}

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
