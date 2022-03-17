from django.shortcuts import render
from .models import PostBlog

# Create your views here.
def blog(request):
    posts = PostBlog.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})
