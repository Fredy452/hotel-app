"""Hotel views."""

# Django
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

# Models
from apps.hotel.models import Hotel, Room, Booking
from apps.user.models import User


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


def hotel_contact(request):
    """
    Función de vista contact
    """
    hotel = Hotel.objects.get(id=1)

    context = {
        'hotel': hotel,
    }
    return render(request, 'hotel/hotel_contact.html', context)


def room_reservation(request, user_id: int, room_id: int):
    """
    Función para reservar una habitación.
    La URL es: /hotel/room/<int:room_id>/reservation/<int:user_id>/
    
    Args:
        request:
        user_id (int): ID del usuario que reserva la habitación.
        room_id (int): ID de la habitación a reservar.

    Returns:
        redirect: Redirecciona a la página...
    """

    if request.method == 'POST':
        # Obtener los datos del formulario
        check_in_date = request.POST['check_in_date']  # Fecha de llegada
        check_out_date = request.POST['check_out_date']  # Fecha de salida

        # Validar que la fecha de llegada sea menor a la de salida
        if check_in_date > check_out_date:
            # TODO: Mostrar un mensaje de error. Utilizar el framework de mensajes de Django.
            return redirect(reverse_lazy('hotel:rooms_details', args=[room_id]))
        
        # Buscar la habitación
        room = Room.objects.get(id=room_id)

        # Buscar el usuario
        user = User.objects.get(id=user_id)

        # Crear la reserva
        Booking.objects.create(
            room=room,
            user=user,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            status='outstanding',
            total_price=0  # TODO: calcular el precio final
        )

        # Redireccionar a la página de reservas
        return redirect('hotel:room_reservation_list', user_id=user_id)


def room_reservation_details(request, user_id: int, booking_id: int):
    """
    Función para mostrar el detalle de la reserva (como un ticket).
    La URL es: /hotel/reservation/<int:user_id>/<int:booking_id>/
    """

    pass
        
        
def room_reservation_list(request, user_id: int):
    """
    Función para mostrar todas las reservas de un usuario.
    La URL es: /hotel/reservation/<int:user_id>/

    Args:
        request: Objeto request de Django.
        user_id (int): ID del usuario que reservó la habitación.

    Returns:
        render: Renderiza la página de reservas.
    """
    
    # Obtener las reservas del usuario
    bookings = Booking.objects.filter(user=user_id)
    context = {'bookings': bookings}

    return render(request, 'hotel/room_reservation_list.html', context)
