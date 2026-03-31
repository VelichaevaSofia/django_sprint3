from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category
from datetime import datetime


def index(request):
    template = 'blog/index.html'

    post_list = Post.objects.all().filter(
        pub_date__lte=datetime.now()).filter(
            is_published=True).filter(
                category__is_published=True)[:5]

    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.all().filter(
            category__is_published=True).filter(
                pub_date__lte=datetime.now()).filter(
                    is_published=True), pk=pk)
    context = {
        "post": post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'

    post_list = Post.objects.all().filter(
        category__slug=category_slug).filter(
            is_published=True).filter(
                pub_date__lte=datetime.now())

    category = get_object_or_404(
        Category.objects.all()
        .filter(slug=category_slug)
        .filter(is_published=True))

    context = {
        "category": category,
        "post_list": post_list
    }
    return render(request, template, context)
