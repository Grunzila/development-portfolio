from __future__ import unicode_literals

from django.db.models.aggregates import Count
from django.db import models
from random import randint

# Create your models here.

class Blurb(models.Model):
    blurb_text = models.CharField(max_length=200)
    
class ItemDocument(models.Model):
    item_text = models.CharField(max_length=32)
    embed_text = models.CharField(max_length=60)
    pub_date = models.DateTimeField('date published')
    
class ItemAudio(models.Model):
    item_text = models.CharField(max_length=32)
    embed_text = models.CharField(max_length=60)
    pub_date = models.DateTimeField('date published')