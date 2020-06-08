from django.conf.urls import url
from .views import *

app_name = 'post'

urlpatterns = [
    url(r'^index/$', post_index , name="index"),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"), #parantez sonrası ?P ifadesi argüman tanımlamak için kullanılır, /d+ ise birden fazla rakam belirteceğini söyler
    url(r'^create/$', post_create, name="create"),
    url(r'^update/$', post_update, name="update"),
    url(r'^delete/$', post_delete, name="delete"),

]
