from brave_cane.api.partner.schemas import Partner
import unittest


class TesteRegisterPartner(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_payload_datatypes(self):
        partner_mock = {
            "id": 13,
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

        self.assertEqual(type(partner_mock['id']), type(0))
        self.assertEqual(type(partner_mock['tradingName']), type(''))
        self.assertEqual(type(partner_mock['ownerName']), type(''))
        self.assertEqual(type(partner_mock['document']), type(''))
        self.assertEqual(type(partner_mock['coverageArea']), dict)
        self.assertEqual(type(partner_mock['address']), dict)
        self.assertEqual(type(partner_mock['coverageArea']['type']), type(''))
        self.assertEqual(type(partner_mock['coverageArea']['coordinates']), list)
        self.assertEqual(type(partner_mock['address']['type']), type(''))
        self.assertEqual(type(partner_mock['address']['coordinates']), list)
        
        for polygons in partner_mock['coverageArea']['coordinates']:
            for polygon in polygons:
                for point in polygon:
                    for p in point:
                        self.assertEqual(type(p), type(0.0))
                        
        for point in partner_mock['address']['coordinates']:
            self.assertEqual(type(point), type(0.0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
