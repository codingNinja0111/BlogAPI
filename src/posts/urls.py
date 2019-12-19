from django.conf.urls import url
from django.contrib import admin
from .views import *




urlpatterns = [
    url(r'^$', posts_list, name='list'),
    url(r'^create/$', posts_create, name='posts_create'),
    url(r'^list/$', posts_list, name='posts_list'),
    url(r'^(?P<id>\d+)/$', posts_details, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', posts_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', posts_delete, name='posts_delete'),
]
