from brave_cane.run import app
from brave_cane.database import session, Base
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
        clear_db(session, Base)
        
    def test_if_method_get_partner_by_coordinates(self):
        lat_mock = float(-23.566360473632812)
        lng_mock = float(-46.6598049774399)

        PartnerManager().get_by_coordinates(lat_mock, lng_mock)


if __name__ == "__main__":
    unittest.main()
