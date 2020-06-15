from graphene import Schema
from brave_cane.api.partner.app_graphql.schemas_graphql import QueryPdv
from brave_cane.api.partner.app_graphql.mutations import MutationPDV

GQLPdv = Schema(query=QueryPdv, mutation=MutationPDV)