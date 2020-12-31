from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def resource(request):

    posts=Post.objects.all()
    return render(request, "resources/resources.html",{"posts":posts})

def category(request, category_id):

    category=Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, "resources/category.html", {'category':category, "posts":posts})