from multiprocessing.resource_tracker import register

from django.contrib import admin,messages

from Shops.models import Category, Product, Site_banner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','name' , 'price' ,'count','best_book' , 'new_book']
    list_editable = ['price' , 'count']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['unfill_score']

    def save_model(self, request, obj, form, change):
        if obj.score < 0 or obj.score > 6:
            messages.error(request, 'قیمت باید بین  0 و 6 باشد')
        else:
            super().save_model(request, obj, form, change)

@admin.register(Site_banner)
class Site_bannerAdmin(admin.ModelAdmin):
    list_display = ['image']