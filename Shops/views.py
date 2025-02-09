from django.shortcuts import render

from Shops.models import Site_banner, Product


def index(request):
    all_banner_img = Site_banner.objects.all()
    all_books = Product.objects.all()
    score_list=[]

    return render(request, 'Shops/index.html' , {'banner_img':all_banner_img , 'books':all_books})
