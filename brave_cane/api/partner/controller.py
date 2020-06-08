from brave_cane.database.models import PDV
from brave_cane.database import session
from brave_cane.conector.mysql import CadastroDBContext

class Partner:
    
    def save(self, pdvs):
        for pdv in pdvs['pdvs']:
            pdv = PDV(**pdv)
            session.add(pdv)
        try:
            session.commit()    
            return {"Status": True, "msg": "All pdvs have been registered."}
        except Exception as e:
            session.rollback()
            session.close()
            return {"Status": False, "msg": "The pdvs couldn't be registered.", "err": str(e)}

    def get_by_id(self, id):
        obj = PDV.get(id=id)
        return obj.as_dict()

    def get_by_coordinates(self, lng, lat):
        pass
