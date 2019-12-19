# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from urllib import quote_plus
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


# Create your views here.
def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # messages.success(request,"Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form":form,
    }
    return render(request,"post_form.html",context)

def posts_details(request,id=None):
    instance = get_object_or_404(Post, id=id)
    share_string = quote_plus(instance.content)
    context = {
    "title":instance.title,
    "instance": instance,
    "context": share_string,
    }

    return render(request,"post_details.html",context)
def posts_list(request):
    # Show 25 contacts per page
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 7)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
    "object_list": queryset,
    "title": "List"
    }
    return render(request,"post_list.html",context)
def posts_update(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
    "title":instance.title,
    "instance": instance,
    "form":form,
    }
    return render(request,"post_form.html",context)
def posts_delete(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("list")
