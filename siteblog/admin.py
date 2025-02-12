from django.contrib import admin

# Register your models here.
from django.contrib import admin

from siteblog.models import SiteBlog


# Register your models here.
@admin.register(SiteBlog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','slug3']
    prepopulated_fields = {'slug3':('token',)}
