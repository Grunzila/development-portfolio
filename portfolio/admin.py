from django.contrib import admin

from .models import Blurb
from .models import ItemDocument
from .models import ItemAudio

# Register your models here.

admin.site.register(Blurb)
admin.site.register(ItemDocument)
admin.site.register(ItemAudio)
