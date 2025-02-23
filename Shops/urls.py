from Shops import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    path('books/newbook/', views.new_book, name='new_book'),
    path('books/bestbook/', views.best_book, name='bestbook'),
    path('login/' , views.login_user, name='login'),
    path('logout/' , views.logout_user, name='logout'),
    path('books/<slug:slug>/', views.book_view, name='book_info'),

]
