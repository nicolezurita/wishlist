from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wish_items/create/$', views.create, name='create'),
    url(r'^add$', views.add, name='add_to_my_list'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='destroy'),
    url(r'^remove/(?P<id>\d+)/(?P<item_name>[\w ]+)/(?P<added_by>[\w ]+)/$', views.remove, name='remove'),
    url(r'^add_to_my_list/(?P<item_name>[\w ]+)/(?P<added_by>[\w ]+)/$', views.add_to_my_list, name='add_to_my_list'),
    url(r'^wish_items/(?P<id>\d+)$', views.show, name='show'),
]
