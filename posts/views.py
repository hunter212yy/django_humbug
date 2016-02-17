from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post

# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'posts/index.html', context)

def detail(request, post_slug):
    post = get_object_or_404(Post, post_slug=post_slug)
    return render(request, 'posts/detail.html', {'post': post})