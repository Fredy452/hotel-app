from django.shortcuts import render, HttpResponse


# Create your views here.
def login(request):
    """
    Funcion de vista `login`
    """
    return render(request, 'auth/login.html')


def register(request):
    """
    Funcion de vista `register`
    """
    return render(request, 'auth/register.html')
