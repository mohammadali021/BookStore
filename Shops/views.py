from django.shortcuts import render

from Shops.models import Site_banner, Product
from siteblog.models import SiteBlog


def index(request):
    all_banner_img = Site_banner.objects.all()
    all_books = Product.objects.all()
    all_blogs = SiteBlog.objects.all().order_by('-id')[:4]


    return render(request, 'Shops/index.html' , {'banner_img':all_banner_img , 'books':all_books , 'blog':all_blogs})
