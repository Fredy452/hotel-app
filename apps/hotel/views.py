"""Hotel views.""""""

# Django
from django.shortcuts import redirect, render

# Models
from apps.hotel.models import Hotel, Room


# Create your views here.
def index(request):
    """
    Funcion de vista principal `hotel-index`
    """
    hotel = Hotel.objects.get(id=1)
    latest_rooms = hotel.room_set.order_by('-id')[:4]

    context = {
        'hotel': hotel,
        'latest_rooms': latest_rooms
    }
    return render(request, 'hotel/hotel_index.html', context)


def hotel_search(request):
    """_summary_

    Args:
        request (_type_): _description_
    """

    pass