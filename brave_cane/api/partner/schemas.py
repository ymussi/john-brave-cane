from marshmallow import fields, Schema, validate

class PointCoordinates(Schema):
    coordinates = fields.List(fields.Number(required=True))

# class MultiPolygonCoordinates(Schema):
#     coordinates = fields.List(required=True)

class Address(Schema):
    type = fields.String(required=True)
    coordinates = fields.Nested(PointCoordinates)

class CoverageArea(Schema):
    type = fields.String(required=True)
    # coordinates = fields.Nested(MultiPolygonCoordinates)
    coordinates = fields.List(fields.String(required=True))

class Partner(Schema):
    id = fields.Integer(description='Id do parceiro.', required=True)
    tradingName = fields.String(required=True)
    ownerName = fields.String(required=True)
    document = fields.String(required=True)
    # coverageArea = fields.Nested(CoverageArea)
    # address = fields.Nested(Address)
    coverageArea = fields.Dict()