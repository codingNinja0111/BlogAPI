# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post


# Create your views here.
def posts_create(request):
    return HttpResponse("<h1>create</h1>")


def posts_details(request,id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
    "title":instance.title,
    "instance": instance,
    }

    return render(request,"post_details.html",context)
def posts_list(request):
    queryset = Post.objects.all()
    context = {
    "object_list": queryset,
    "title": "List"
    }
    return render(request,"index.html",context)
def posts_update(request):
    return HttpResponse("<h1>update</h1>")
def posts_delete(request):
    return HttpResponse("<h1>delete</h1>")
