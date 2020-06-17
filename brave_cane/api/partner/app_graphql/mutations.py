from graphene import ObjectType, InputObjectType, Mutation, InputField, Field, Argument, String, Int, Float, List
from brave_cane.api.partner.app_graphql.resolvers import PartnerResolvers
from brave_cane.api.partner.app_graphql.schemas_graphql import GQLPartner
from graphql import GraphQLError
import re


class GQLInputAddress(InputObjectType):
    type = String(required=True)
    coordinates = List(Float, required=True)

class GQLInputCoverageArea(InputObjectType):
    type = String(required=True)
    coordinates = List(List(List(List(Float, required=True))))

class RegisterPdv(Mutation):
    class Arguments:
        id = Int(required=True)
        tradingName = String(required=True)
        ownerName = String(required=True)
        document = String(required=True)
        coverageArea = Argument(GQLInputCoverageArea, required=True)
        address = Argument(GQLInputAddress, required=True)
    
    pdvs = Field(lambda : GQLPartner)
    
    @staticmethod
    def mutate(self, info, id=None, tradingName=None, ownerName=None,
               document=None, coverageArea=None, address=None):
        
        pdv = GQLPartner(id=id, tradingName=tradingName, ownerName=ownerName, 
                         document=document, coverageArea=coverageArea, address=address)
        
        save_pdv = PartnerResolvers().pdv_resolver_save_pdv(id=id, tradingName=tradingName, ownerName=ownerName, 
                         document=document, coverageArea=coverageArea, address=address)
        
        # if save_pdv['status'] == False:
        if not save_pdv:
            raise GraphQLError(f'{save_pdv["msg"]} - err: {save_pdv["err"]}')
        
        return RegisterPdv(pdvs=pdv)
    
class MutationPDV(ObjectType):
    register_pdv = RegisterPdv.Field()