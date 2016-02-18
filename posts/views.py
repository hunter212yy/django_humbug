from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post, Tag

# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    index_paginator = Paginator(latest_post_list, 3)
    page = request.GET.get('page')
    
    try:
        kek = index_paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        kek = index_paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        kek = index_paginator.page(index_paginator.num_pages)
    
    return render(request, 'posts/index.html', {'latest_post_list': kek, 'kek': kek})

def detail(request, post_slug):
    post = get_object_or_404(Post, post_slug=post_slug)
    return render(request, 'posts/detail.html', {'post': post})

def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, tag_slug=tag_slug)
    paginator = Paginator(tag.post_set.all(), 2)
    
    page = request.GET.get('page')
    try:
        shit = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        shit = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        shit = paginator.page(paginator.num_pages)
    
    return render(request, 'posts/index.html', {'latest_post_list': shit, 'tag': tag, 'shit': shit})