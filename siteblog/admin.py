from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import admin
from siteblog.models import SiteBlog


# Register your models here.
@admin.register(SiteBlog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    # prepopulated_fields = {'slug3':('token',)}
    readonly_fields = ['slug']
