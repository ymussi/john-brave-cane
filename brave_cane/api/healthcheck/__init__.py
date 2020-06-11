from brave_cane.database.models import PDV
from brave_cane.database import session

def get_first_partner():
    try:
        obj = session.query(PDV.id).first()
        session.close()
        if obj.id is not None:
            response = {
                    'message': 'The request was fulfilled.'}
            status_code = 200
            return response, status_code
    except Exception as e:
        response = {'message': 'The request had bad syntax or was inherently impossible to be satisfied.',
                    'err': str(e)}
        status_code = 400
        return response, status_code
    