from django.shortcuts import render

from Shops.models import Site_banner, Product
from siteblog.models import SiteBlog


def index(request):
    all_banner_img = Site_banner.objects.all()
    New_book = Product.objects.filter(new_book=True).order_by("-id")[:6]
    Best_books = Product.objects.filter(best_book=True).order_by("-id")[:6]
    all_blogs = SiteBlog.objects.all().order_by('-id')[:4]


    return render(request, 'Shops/index.html' , {'banner_img':all_banner_img 
                                                  , 'blog':all_blogs , 'newbook':New_book ,'bestbook':Best_books})

def book_view(request):
    return render(request , 'Shops/book.html')