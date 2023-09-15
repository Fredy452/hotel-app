from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    """
    Funcion de vista principal `hotel-index`
    """
    return HttpResponse("You are in the index view")
