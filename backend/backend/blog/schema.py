from backend.backend.blog import queries
import graphene
from graphene_django.types import DjangoObjectType
from blog import models
from blog import types
from django.contrib.auth import get_user_model

# Define type
class Sitetype(DjangoObjectType):
    class Meta:
        model = models.Site

# The Query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType)

    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )

schema = graphene.Schema(query=queries.Query)