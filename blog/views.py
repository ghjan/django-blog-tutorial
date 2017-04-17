# encoding: utf-8
import markdown

from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from . import cache_manager

"""
使用下方的模板引擎方式。
def index(request):
    return HttpResponse("欢迎访问我的博客首页！")
"""

"""
使用下方真正的首页视图函数
def index(request):
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
"""


def index(request):
    post_list = Post.objects.all()
    for post in post_list:
        post.click = cache_manager.get_click(post)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    #更新缓存
    cache_manager.update_click(post)
    post.click = cache_manager.get_click(post)
    #同步数据库
    cache_manager.sync_click()
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})


# def post_list(request):
#     """所有已发布文章"""
#     posts = Post.objects.annotate(num_comment=Count('comment')).filter(
#         published_date__isnull=False).prefetch_related(
#         'category').prefetch_related('tags').order_by('-published_date')
#     for p in posts:
#         p.click = cache_manager.get_click(p)
#     return render(request, 'blog/post_list.html', {'posts': posts})
#
# def post_detail(request, pk):
#     try:
#         pass
#     except:
#         raise Http404()
#     if post.published_date:
#         cache_manager.update_click(post)
#         post.click = cache_manager.get_click(post)