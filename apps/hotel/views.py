"""Hotel views."""

# Django
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse

# Python
import datetime

# Models
from apps.hotel.models import Hotel, Room, Booking
from apps.user.models import User, Profile

# Form
from apps.hotel.forms import ReservationForm


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


def hotel_contact(request):
    """
    Función de vista contact
    """
    hotel = Hotel.objects.get(id=1)

    context = {
        'hotel': hotel,
    }
    return render(request, 'hotel/hotel_contact.html', context)


def rooms_details(request, room_id):
    """
    Función de vista para los detalles de una habitación.
    """
    try:
        # Obteniendo fecha actual
        today = datetime.date.today()

        if request.method == 'POST':
            # Obtener los datos del formulario
            form = ReservationForm(request.POST)
            # Buscar la habitación
            room = Room.objects.get(id=room_id)

            # Verificar si el usuario está autenticado
            if not request.user.is_authenticated:
                messages.warning(request, 'Debes iniciar sesión para realizar una reserva.')
                return redirect(reverse_lazy('hotel:rooms_details', args=[room_id]))

            # Buscar el usuario
            user = User.objects.get(id=request.user.id)
            if form.is_valid():
                check_in_date = form.cleaned_data['check_in_date']  # Fecha de llegada
                check_out_date = form.cleaned_data['check_out_date']  # Fecha de salida

                # Validar que la fecha de llegada sea menor a la de salida
                if check_in_date > check_out_date:
                    messages.warning(request, '¡El check out debe ser posterior a la fecha de entrada!')
                    return redirect(reverse_lazy('hotel:rooms_details', args=[room_id]))

                # Calculando el precio total
                duration = check_out_date - check_in_date
                room_price = room.price
                total_price = room_price * duration.days

                # Crear la reserva
                Booking.objects.create(
                    room=room,
                    user=user,
                    check_in_date=check_in_date,
                    check_out_date=check_out_date,
                    status='outstanding',
                    total_price=total_price
                )

                # Redireccionar a la página de reservas
                return redirect('hotel:room_reservation_list', user_id=user.id)

        hotel = Hotel.objects.get(id=1)
        room = hotel.room_set.get(id=room_id)

        context = {
            'hotel': hotel,
            'room': room,
            'today': today
        }
        return render(request, 'hotel/hotel_rooms_details.html', context)

    except Hotel.DoesNotExist:
        # Manejar el caso en el que no se encuentra el hotel
        messages.error(request, 'La habitación no existe.')
        return redirect(reverse_lazy('hotel:index'))  # Redirigir a la página principal u otra página adecuada


def room_reservation_details(request, user_id: int, booking_id: int):
    """
    Función para mostrar el detalle de la reserva (como un ticket).
    La URL es: /hotel/reservation/<int:user_id>/<int:booking_id>/
    """
    reservation = Booking.objects.get(id=booking_id)
    hotel = Hotel.objects.get(id=1)

    context = {
        'hotel': hotel,
        'reservation': reservation
    }
    return render(request, 'hotel/room_reservation_details.html', context)


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

    # Obteniedo hotel
    hotel = Hotel.objects.get(id=1)

    # Obteniendo el usuario y el perfil
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)

    # Obtener las reservas del usuario
    bookings = Booking.objects.filter(user=user_id)

    # Verificar si es una solicitud AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Crear una lista de diccionarios con los datos de las reservas
        bookings_data = []
        for booking in bookings:
            booking_data = {
                'room_number': booking.room.number,
                'room_type': booking.room.type,
                'check_in_date': booking.check_in_date.strftime("%Y-%m-%d"),
                'check_out_date': booking.check_out_date.strftime("%Y-%m-%d"),
                'status': booking.status,
                'total_price': booking.total_price,
            }
            bookings_data.append(booking_data)
        # Devolver los datos JSON como respuesta
        return JsonResponse({'data': bookings_data})
    else:
        # Si no es una solicitud ajax devolvemos el contexto
        context = {
            'bookings': bookings,
            'user': user,
            'profile': profile,
            'hotel': hotel
        }

        return render(request, 'hotel/room_reservation_list.html', context)


def room_reservation_cancel(request, booking_id, user_id):
    """
    Funcion de vista para cancelar reservas
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = "cancelado"
    booking.save()
    messages.warning(request, 'Reserva Cancelada')
    return redirect(reverse_lazy('hotel:room_reservation_list', args=[user_id]))
