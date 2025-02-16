from django.urls import path

from siteblog.views import index, blog_page

urlpatterns = [
    path('', blog_page, name='blog_page'),
    path('<slug:slug>/', index,name = 'blog'),

]