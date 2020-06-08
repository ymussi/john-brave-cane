from brave_cane.database.models import Partner
from brave_cane.database import engine
from brave_cane.conector.mysql import CadastroDBContext

class Partner:

    def save(self, pdvs):
        try:
            with CadastroDBContext(engine) as db:
                for pdv in pdvs['pdvs']:
                    part = Partner(**pdv)
                    db.session.add(part)
                db.session.commit()
            
            return {"Status": True, "msg": "All pdvs have been registered."}
        except Exception as e:
            return {"Status": False, "msg": "The pdvs couldn't be registered.", "err": str(e)}

    def get_by_id(self, id):
        pass

    def get_by_coordinates(self, lng, lat):
        pass
