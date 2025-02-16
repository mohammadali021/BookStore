from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

import Shops
from Shops.models import Site_banner, Product
from siteblog.models import SiteBlog


def index(request):
    all_banner_img = Site_banner.objects.all()
    New_book = Product.objects.filter(new_book=True).order_by("-id")[:6]
    Best_books = Product.objects.filter(best_book=True).order_by("-id")[:6]
    all_blogs = SiteBlog.objects.all().order_by('-id')[:4]


    return render(request, 'Shops/index.html' , {'banner_img':all_banner_img 
                                                  , 'blog':all_blogs , 'newbook':New_book ,'bestbook':Best_books})

def book_view(request , slug):
    # book = get_object_or_404(SiteBlog, slug=slug)
    book = Product.objects.filter(slug=slug)
    return render(request , 'Shops/book.html', {'book':book})

def new_book(request):
    newb = Product.objects.all().order_by("-id")
    paginator = Paginator(newb , 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request , 'Shops/new_books.html' , {'newbook':page_obj})