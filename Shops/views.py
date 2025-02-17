from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

import Shops
from Shops.models import Site_banner, Product
from siteblog.models import SiteBlog


def index(request):
    all_banner_img = Site_banner.objects.all()
    New_book = Product.objects.filter(new_book=True).order_by("-id")[:6]
    Best_books = Product.objects.filter(best_book=True).order_by("-id")[:6]
    all_blogs = SiteBlog.objects.all().order_by('-id')[:4]

    return render(request, 'Shops/index.html', {'banner_img': all_banner_img
        , 'blog': all_blogs, 'newbook': New_book, 'bestbook': Best_books})


def book_view(request, slug):
    # book = get_object_or_404(SiteBlog, slug=slug)
    book = Product.objects.filter(slug=slug)
    return render(request, 'Shops/book.html', {'book': book})


def new_book(request):
    newb = Product.objects.filter(new_book=True).order_by("-id")
    paginator = Paginator(newb, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Shops/new_books.html', {'newbook': page_obj})


def best_book(request):
    best = Product.objects.filter(best_book=True).order_by("-id")
    paginator = Paginator(best, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "Shops/best_book.html", {'bestbook': page_obj})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'ورود موفقیت آمیز بود')
            if username=='admin':
                return redirect('admin:index')
            return redirect('home')
        else:
            messages.error(request , 'لطفا ابتدا در سایت ثبت نام نمایید ')
            return redirect('home')

#
def logout_user(request):
    logout(request)
    return redirect('home')
