from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    """
    Funcion de vista principal `hotel-index`
    """
    return render(request, 'hotel/hotel_index.html')
