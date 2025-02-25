from django.conf.urls.static import static
from django.urls import path

from BookStore import settings
from users.views import register, dashboard, edit_profile

urlpatterns = [
    path('' , register , name='register'),
    path('profile/<slug:slug>/' , dashboard , name='profile'),
    path('edit_info/' , edit_profile , name='edit_profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



