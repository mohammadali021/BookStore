from django.urls import path

from siteblog.views import index

urlpatterns = [
    path('<slug:slug>/', index,name = 'blog'),
    # path('<slug:slug>/<str:title>/', index,name = 'blogbytitle')
]