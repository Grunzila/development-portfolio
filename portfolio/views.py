from django.shortcuts import get_object_or_404, render
from django.views import generic
import random

# Create your views here.

from .models import Blurb, ItemDocument, ItemAudio

class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    model = Blurb
    
    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['audio'] = ItemAudio.objects.all()
        ctx['document'] = ItemDocument.objects.all()
        return ctx
        
    
class DocumentView(generic.DetailView):
    template_name = 'portfolio/document.html'
    model = ItemDocument
    
class AudioView(generic.DetailView):
    template_name = 'portfolio/audio.html'
    model = ItemAudio