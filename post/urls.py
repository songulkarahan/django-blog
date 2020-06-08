from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$', post_index),
    url(r'^(?P<id>\d+)/$', post_detail), #parantez sonrası ?P ifadesi argüman tanımlamak için kullanılır, /d+ ise birden fazla rakam belirteceğini söyler
    url(r'^create/$', post_create),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),

]
