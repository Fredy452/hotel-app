"""Hotel views."""

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
    if request.method == 'POST':
        print(request.POST['check_in_date'])
        return redirect('hotel:index')

    else:
        return redirect('hotel:index')


def rooms(request):
    """
    Funcion de vista rooms
    """
    hotel = Hotel.objects.get(id=1)
    all_rooms = hotel.room_set.all()

    context = {
        'hotel': hotel,
        'all_rooms': all_rooms
    }

    return render(request, 'hotel/hotel_rooms.html', context)


def rooms_details(request, room_id):
    """
    Funcion de vita room details
    """
    hotel = Hotel.objects.get(id=1)
    room = hotel.room_set.get(id=room_id)

    context = {
        'hotel': hotel,
        'room': room
    }

    return render(request, 'hotel/hotel_rooms_details.html', context)