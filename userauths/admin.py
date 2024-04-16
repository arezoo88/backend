from django.contrib import admin
from userauths.models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'gender']
    list_editable = ['gender']
    # search_fields = ['gender']

    def get_full_name(self, obj):
        return obj.user.full_name
