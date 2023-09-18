from django.contrib import admin
from django.utils.html import format_html
from .models import Profile


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'display_profile_image')

    def display_profile_image(self, obj):
        if obj.profile:
            return format_html(
                '<div style="width: 50px; height: 50px; overflow: hidden; border-radius: 50%;"><img src="{}" '
                'style="width: 100%; height: auto;"></div>',
                obj.profile.url)
        else:
            return "No profile image"

    display_profile_image.short_description = 'Profile Image'


admin.site.register(Profile, ProfileAdmin)
