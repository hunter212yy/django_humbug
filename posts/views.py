from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Post

# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)

def detail(request, post_slug):
    try:
        post = Post.objects.get(pk=post_slug)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'posts/detail.html', {'post': post})