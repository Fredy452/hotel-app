"""Hotel admin."""

# Django
from django.contrib import admin
from django.utils.html import format_html

# Models
from apps.hotel.models import Hotel, Room, Booking


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'display_logo_image')

    def display_logo_image(self, obj):
        if obj.logo:
            return format_html(
                '<div style="width: 50px; height: 50px; overflow: hidden; border-radius: 50%;"><img src="{}" '
                'style="width: 100%; height: auto;"></div>',
                obj.logo.url)
        else:
            return "No logo image"

    display_logo_image.short_description = 'Logo'


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'number', 'type', 'availability', 'price', 'display_img')

    def display_img(self, obj):
        if obj.img:
            return format_html(
                '<div style="width: 50px; height: 50px; overflow: hidden;"><img src="{}" '
                'style="width: 100%; height: auto;"></div>',
                obj.img.url)
        else:
            return "No hay imagen"

    display_img.short_description = 'Imagen'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Booking admin class."""

    list_display = ('user', 'check_in_date', 'check_out_date', 'status', 'total_price')
