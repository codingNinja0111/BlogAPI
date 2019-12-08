from django.conf.urls import url
from django.contrib import admin
from .views import *




urlpatterns = [
    url(r'^$', posts_list, name='posts_list'),
    url(r'^create/$', posts_create, name='posts_create'),
    # url(r'^list/$', posts_list, name='posts_list'),
    url(r'^details/$', posts_details, name='posts_detail'),
    url(r'^update/$', posts_update, name='posts_update'),
    url(r'^delete/$', posts_delete, name='posts_delete'),
]
