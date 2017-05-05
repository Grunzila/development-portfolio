from django.shortcuts import get_object_or_404, render
from django.views import generic

# Create your views here.

from .models import Blurb, ItemDocuments, ItemAudio

class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    model = Blurb, ItemDocuments, ItemAudio