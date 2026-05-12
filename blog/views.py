
from django.shortcuts import render
from .models import User, Category, Post, Comment


def main(request):
    return render(request, 'main.html')


def users(request):
    all_users = User.objects.all()
    context = {'users': all_users}
    return render(request, 'users.html', context)


def categories(request):
    all_categories = Category.objects.all()
    context = {'categories': all_categories}
    return render(request, 'categories.html', context)


def blogs(request):
    all_posts = Post.objects.all()
    context = {'posts': all_posts}
    return render(request, 'blogs.html', context)


def blogdetails(request, id):
    single_post = Post.objects.get(id=id)
    context = {'post': single_post}
    return render(request, 'blogdetails.html', context)


def comments(request):
    all_comments = Comment.objects.all()
    context = {'comments': all_comments}
    return render(request, 'comments.html', context)