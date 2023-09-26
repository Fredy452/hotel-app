from django.urls import path
from apps.hotel.views import (index, hotel_search, rooms, rooms_details,
                              hotel_contact, room_reservation_list, room_reservation_details, room_reservation_cancel)  # noqa: E501


# App name
app_name = 'hotel'

urlpatterns = [
    path('', index, name="index"),
    path('hotel/search/', hotel_search, name="search"),
    path('hotel/rooms/', rooms, name="rooms"),
    path('hotel/room/<int:room_id>/details/', rooms_details, name='rooms_details'),
    path('hotel/contact/', hotel_contact, name='contact'),
    path(
        'hotel/reservation/<int:user_id>/',
        room_reservation_list,
        name='room_reservation_list',
    ),
    path(
        'hotel/reservation/user/<int:user_id>/reservation/<int:booking_id>',
        room_reservation_details,
        name="reservation_detail"
    ),
    path(
        'hotel/reservation/user/<int:user_id>/reservation/<int:booking_id>/cancel',
        room_reservation_cancel,
        name="reservation_cancel"
    )
]
