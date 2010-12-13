from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

class OrderedRelation(models.Model):
    """
    """
    order = models.IntegerField()

    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
