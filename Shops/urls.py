

from Shops import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='home'),
    # path('books/<slug:slug>/', views.book_view, name='book_view'),
    path('books/<slug:slug>/', views.book_view, name='book_info'),
    path('newbook/', views.new_book, name='new_book'),

]

