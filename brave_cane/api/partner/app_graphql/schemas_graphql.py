from graphene import ObjectType, InputObjectType, Mutation, Schema, InputField, Field, Argument, JSONString, String, Int, Float, List
from brave_cane.api.partner.app_graphql.resolvers import PartnerResolvers
from graphql import GraphQLError


class GQLAddress(ObjectType):
    type = String(required=True)
    coordinates = List(Float, required=True)

class GQLCoverageArea(ObjectType):
    type = String(required=True)
    coordinates = List(List(List(List(Float, required=True))))

class GQLPartner(ObjectType):
    id = Int(required=True)
    tradingName = String(required=True)
    ownerName = String(required=True)
    document = String(required=True)
    coverageArea = Field(GQLCoverageArea,)
    address = Field(GQLAddress,)

class QueryPdv(ObjectType):

    pdvs = Field(GQLPartner, id=Int(), lat=Float(), lng=Float())

    def resolve_pdvs(self, info, id=None, lat=None, lng=None):
        resolvers = PartnerResolvers()
        if id is not None:
            pdv = resolvers.pdv_resolver_get_by_id(id=id)
        else:
            pdv = resolvers.pdv_resolver_get_by_coordinates(lat, lng)
        
        if "status" in pdv:
            if pdv['status'] == False:
                raise GraphQLError(pdv['msg'])
            
        return GQLPartner(**pdv)
