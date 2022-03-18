from django.shortcuts import render
from .models import PostBlog
from django.views.generic import DetailView

# Create your views here.
def blog(request):
    posts = PostBlog.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

class BlogDetail(DetailView):
    model = PostBlog
    template_name = 'blog/details_view.html'
    context_object_name = 'blogs_str'
