from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Blurb(models.Model):
    blurb_text = models.CharField(max_length=200)
    
class Item(models.Model):
    item_text = models.CharField(max_length=32)
    pub_date = models.DateTimeField('date published')
    
class Visits(models.Model):
    visits = models.IntegerField(default=0)