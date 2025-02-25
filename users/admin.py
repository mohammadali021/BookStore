from django.contrib import admin

from users.models import UserPannel

@admin.register(UserPannel)
class UserPannelAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'slug')

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'

