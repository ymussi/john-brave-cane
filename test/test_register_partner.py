from brave_cane.run import app
from brave_cane.database import session, Base
from brave_cane.database.models import PDV
from brave_cane.api.partner.controller import PartnerManager

from test.runner import clear_db
import unittest


class TesteRegisterPartner(unittest.TestCase):

    def setUp(self):
        self.app_context = app.test_request_context()
        self.app_context.push()
        app.test_client()
        self.app = app

    def tearDown(self):
        pass

    def test_if_save_method_saves_partners_on_database(self):
        partner_mock = {
            "id": 29,
            "tradingName": "Teste",
            "ownerName": "Teste",
            "document": "00000000000191",
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [[[-23.562256297264703, -46.66099548339844],
                        [-23.562256297264703, -46.662025451660156],
                        [-23.57358496022532, -46.6644287109375],
                        [-23.58853100613786, -46.65721893310547],
                        [-23.585069967982925, -46.63747787475586],
                        [-23.58082220549596, -46.63061141967774],
                        [-23.568392777659398, -46.631126403808594],
                        [-23.56005338823039, -46.64073944091797],
                        [-23.562256297264703, -46.66099548339844]]],
                    [[[-23.589946859072384, -46.655845642089844],
                        [-23.59167732524408, -46.654987335205085],
                        [-23.59073343743435, -46.655845642089844],
                        [-23.601430434940486, -46.642799377441406],
                        [-23.597969737092242, -46.62185668945313],
                        [-23.589946859072384, -46.622714996337905],
                        [-23.58569925443702, -46.62872314453126],
                        [-23.588688323885066, -46.63970947265626],
                        [-23.589946859072384, -46.655845642089844]]],
                    [[[-23.574686305893117, -46.681766510009766],
                        [-23.584912645897916, -46.682624816894524],
                        [-23.595924736349982, -46.66614532470703],
                        [-23.57924892524502, -46.66322708129883],
                        [-23.57437163664494, -46.68039321899414],
                        [-23.574686305893117, -46.681766510009766]]]
                        ]
                },
            "address": {
                "type": "Point",
                "coordinates": [-23.58748249, -46.67235334]
                }
            }

        pdv = PDV(**partner_mock)
        session.add(pdv)
        session.commit()

        _model = PDV.get(id=29)
        self.assertIsNotNone(_model)


if __name__ == "__main__":
    unittest.main()
