from brave_cane.api.partner.models import Partner
from brave_cane.seeds.custom_generators import NameGenerator, StateGeneratorSequence
from flask_seeder import Seeder, Faker, generator
import geojson


class PartnerSeeder(Seeder):

    def run(self):
        faker_for_partner = Faker(
            cls=Partner,
            init={
                "tradingName": f"Adega da Cerveja - {StateGeneratorSequence()}",
                "ownerName": NameGenerator().generate(),
                "document": "1432132123891/0001",
                "coverageArea": {
                    "type": "MultiPolygon",
                    "coordinates": [
                        geojson.utils.generate_random(
                            "Polygon")['coordinates'],
                        geojson.utils.generate_random(
                            "Polygon")['coordinates'],
                        geojson.utils.generate_random("Polygon")['coordinates']
                        ]
                },
                "address": {
                    "type": "Point",
                    "coordinates": geojson.utils.generate_random("Point")['coordinates']
                },
            }
        )

        for partner in faker_for_partner.create(5):
            print("Adding partner: %s" % partner)
            self.db.session.add(partner)
