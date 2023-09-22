from django.urls import path, include
from apps.hotel.views import index, hotel_search, rooms, rooms_details

app_name = 'hotel'


urlpatterns = [
    path('', index, name="index"),
    path('hotel/search', hotel_search, name="search"),
    path('hotel/rooms', rooms, name="rooms"),
    path('hotel/room/<int:room_id>/details', rooms_details, name="rooms_details")
]