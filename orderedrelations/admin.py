from django.contrib.contenttypes import generic
from orderedrelations.models import OrderedRelation

class OrderedRelationInline(generic.GenericTabularInline):
    extra = 1
    model = OrderedRelation

class OrderedRelationAdminMixin(object):
    inlines = [
        OrderedRelationInline,
    ]
