from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from siteblog.models import SiteBlog
from django.core.paginator import Paginator

# Create your views here.

def index(request , slug , title=None):

    post = get_object_or_404(SiteBlog, slug=slug)
    if title:
        if post.title != title:
            return HttpResponse(request , '404ss')
    return render(request , 'site_blogs/blog.html' , {"post": post})

def blog_page(request):
    blog = SiteBlog.objects.all().order_by("-id")
    paginator = Paginator(blog , 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request , 'site_blogs/blogpage.html' , {"blog": page_obj})
