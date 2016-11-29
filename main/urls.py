from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^pokemon/([0-9]+)/?$', views.pokemon_specific),
]