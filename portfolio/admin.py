from django.contrib import admin

from .models import Blurb
from .models import ItemDocuments
from .models import ItemAudio

# Register your models here.

admin.site.register(Blurb)
admin.site.register(ItemDocuments)
admin.site.register(ItemAudio)
