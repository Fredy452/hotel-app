from django.urls import path, include
from apps.hotel.views import index

app_name = 'hotel'


urlpatterns = [
    path('', index, name="index")
]