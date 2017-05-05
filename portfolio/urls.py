from django.conf.urls import url

from . import views

app_name = 'portfolio'
urlpatterns = [
    # ex: /
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /document/5/
    url(r'^document/(?P<pk>[0-9]+)/$', views.DocumentView.as_view(), name='document'),
    # ex: /audio/5/
    url(r'^audio/(?P<pk>[0-9]+)/$', views.AudioView.as_view(), name='audio'),
]