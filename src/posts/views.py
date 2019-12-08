# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def posts_create(request):
    return HttpResponse("<h1>create</h1>")
def posts_details(request):
    return HttpResponse("<h1>details</h1>")
def posts_list(request):
    context = {
    "title": "List"
    }
    return render(request,"index.html",context)
def posts_update(request):
    return HttpResponse("<h1>update</h1>")
def posts_delete(request):
    return HttpResponse("<h1>delete</h1>")
