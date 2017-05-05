from django.shortcuts import get_object_or_404, render
from django.views import generic

# Create your views here.

from .models import Blurb, ItemDocuments, ItemAudio

class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    model = Blurb#, ItemDocuments, ItemAudio
    
class DocumentView(generic.DetailView):
    template_name = 'portfolio/document.html'
    model = ItemDocuments
    
class AudioView(generic.DetailView):
    template_name = 'portfolio/audio.html'
    model = ItemAudio