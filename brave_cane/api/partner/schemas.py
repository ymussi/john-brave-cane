from marshmallow import fields, Schema, validate

class Address(Schema):
    type = fields.String(required=True)
    coordinates = fields.List(fields.Float(required=True))

class CoverageArea(Schema):
    type = fields.String(required=True)
    coordinates = fields.List(fields.List(fields.List(fields.List(fields.Integer(required=True)))))

class Partner(Schema):
    id = fields.Integer(description='Id do parceiro.', required=True)
    tradingName = fields.String(required=True)
    ownerName = fields.String(required=True)
    document = fields.String(required=True)
    coverageArea = fields.Nested(CoverageArea)
    address = fields.Nested(Address)

class Pdvs(Schema):
    pdvs = fields.List(fields.Nested(Partner))

class PartnerByID(Schema):
    id = fields.Integer(description='Id do parceiro.', required=True)

