from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from d3matt.views import LINKS
from blog.forms import AddBlogForm


@login_required
def addblog(request, *args, **kwargs):
    if request.POST:
        form = AddBlogForm(request.POST)
        if form.is_valid():
            return redirect('/d3matt/')
    else:
        form = AddBlogForm()
    return render_to_response('addblog.html', {'form': form, 'LINKS': LINKS}, context_instance=RequestContext(request))
