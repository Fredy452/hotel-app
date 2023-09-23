from django.urls import path
from apps.hotel.views import index, hotel_search, rooms, rooms_details, hotel_contact, room_reservation, room_reservation_list  # noqa: E501


# App name
app_name = 'hotel'

urlpatterns = [
    path('', index, name="index"),
    path('hotel/search', hotel_search, name="search"),
    path('hotel/rooms', rooms, name="rooms"),
    path('hotel/room/<int:room_id>/details', rooms_details, name='rooms_details'),
    path('hotel/contact', hotel_contact, name='contact'),
    path(
        'hotel/room/<int:room_id>/reservation/<int:user_id>/',
        room_reservation,
        name='room_reservation',
    ), 
    path(
        'hotel/reservation/<int:user_id>/',
        room_reservation_list,
        name='room_reservation_list',
    )
]
