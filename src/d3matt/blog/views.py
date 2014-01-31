from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import Http404, HttpResponse

from d3matt.views import LINKS
from blog.forms import AddBlogForm, EditBlogForm, EditDraftBlogForm
from blog.models import BlogPost

import json
import sys


@login_required
def addblog(request, *args, **kwargs):
    if request.POST:
        form = AddBlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.draft = False
            post.edited = False
            if 'save_draft' in request.POST:
                post.draft = True
            post.author = request.user
            post.save()
            return redirect('/d3matt/')
    else:
        form = AddBlogForm()
    return render_to_response('blogform.html', {'form': form, 'form_type': 'Add Blog Post', 'LINKS': LINKS}, context_instance=RequestContext(request))

@login_required
def editblog(request, *args, **kwargs):
    post = get_object_or_404(BlogPost, id=kwargs["blog"])
    if request.POST:
        form = EditBlogForm(request.POST, instance=post)
        if form.is_valid():
            newpost = form.save(commit=False)
            if post.draft:
                if 'save_draft' in request.POST:
                    newpost.draft = True
                else:
                    newpost.draft = False
            else:
                newpost.edited = True
            newpost.save()
            return redirect('/d3matt/')
    else:
        if post.draft:
            form = EditDraftBlogForm(instance = post)
        else:
            form = EditBlogForm(instance = post)
    return render_to_response('blogform.html', {'form': form, 'form_type': 'Edit Blog Post', 'LINKS': LINKS}, context_instance=RequestContext(request))

def jsonblog(request, *args, **kwargs):
    post = get_object_or_404(BlogPost, id=kwargs['blog'])
    cont = {}
    cont['title'] = post.title
    cont['content'] = post.content
    response = HttpResponse(content_type='text/json; charset=utf-8')
    json.dump(cont, response, indent=4)
    return response
