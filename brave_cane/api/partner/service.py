# from brave_cane.api.partner.controller import Partner
from brave_cane.database.models import PDV
from math import radians, cos, sin, asin, sqrt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from werkzeug.exceptions import BadRequest, UnprocessableEntity

class PartnerServices:

    def distance_between_points(self, a, b):
        # Land radius in km
        r = 6371
        
        lon1, lat1, lon2, lat2 = map(radians, [a['lng'], a['lat'], b['lng'], b['lat']])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        hav = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        distance = 2 * r * asin( sqrt(hav))

        return distance
    
    def format_polygon(self, polygon):
        multiPolygonsFormated = []
        for point in polygon[0]:
            multiPolygonsFormated.append(tuple(point))
            
        return multiPolygonsFormated
    
    def format_point(self, point):
        lat = float(point['lat'])
        lng = float(point['lng'])
        
        return (lat, lng)
    
    def client_contains_area(self, partner, client):        
        point = Point(client)
        polygon = Polygon(partner)
        
        return polygon.contains(point)

    def check_partner_area(self, pdvs, client):
        partner = []
        for pdv in pdvs:
            multipolygon = pdv['coverageArea']['coordinates']
            for polygon in multipolygon:
                contains = self.client_contains_area(self.format_polygon(polygon), self.format_point(client))
                if contains:
                    partner.append(pdv['id'])
                    
        return partner

    def get_nearest_partner(self, partners, client):
        nearest = self.check_partner_area(partners, client)
        distances = []
        for pdv in nearest:
            partner = PDV.get(id=pdv).as_dict()
            coordinates = partner['address']['coordinates']
            p = {'lat': float(coordinates[0]), 'lng': float(coordinates[1])}
            distance = self.distance_between_points(client, p)
            distances.append({'id': pdv, 'distance': distance})
            
        if distances:
            nearest = sorted(distances, key=lambda k: k['distance'])[0]
            nearest_partner = PDV.get(id=nearest['id']).as_dict()
            
            return nearest_partner
        else:
            raise BadRequest('Coordinates outside the coverage area of our partners.')
    