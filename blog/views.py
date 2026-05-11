from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Category, Post, Comment
# Create your views here.

# 1. الصفحة الرئيسية (لا تحتاج بيانات من قاعدة البيانات)
def main(request):
    return render(request, 'main.html')

# 2. صفحة المستخدمين
def users(request):
    # سحب جميع المستخدمين
    all_users = User.objects.all()
    context = {'users': all_users}
    return render(request, 'users.html', context)

# 3. صفحة التصنيفات
def categories(request):
    # سحب جميع التصنيفات
    all_categories = Category.objects.all()
    context = {'categories': all_categories}
    return render(request, 'categories.html', context)

# 4. صفحة قائمة المقالات
def blogs(request):
    # سحب جميع المقالات
    all_posts = Post.objects.all()
    context = {'posts': all_posts}
    return render(request, 'blogs.html', context)

# 5. صفحة تفاصيل مقال محدد (تستقبل id من الرابط)
def blogdetails(request, id):
    # سحب مقال واحد فقط يطابق الـ id
    single_post = Post.objects.get(id=id)
    context = {'post': single_post}
    return render(request, 'blogdetails.html', context)

# 6. صفحة التعليقات
def comments(request):
    # سحب جميع التعليقات
    all_comments = Comment.objects.all()
    context = {'comments': all_comments}
    return render(request, 'comments.html', context)