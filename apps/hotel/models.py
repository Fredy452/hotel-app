"""Hotel models."""

# Django
from django.db import models

# Models
from apps.user.models import User


class Hotel(models.Model):
    """Hoteles."""
    
    name = models.CharField('nombre', max_length=50)
    second_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    description = models.TextField(default="Sin descripción")
    direction = models.CharField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField('teléfono', blank=True, null=True)
    # TODO: acá podrías crear una clase "BaseModel" de la cual hereden las otras clases
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Esto podría ir en "BaseModel"
    updated_at = models.DateTimeField(auto_now=True, null=True)  # Esto podría ir en "BaseModel"

    class Meta:
        """Meta options."""
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'

    def __str__(self):
        """Retorna la propiedad `name`."""
        return self.name


class Room(models.Model):
    """Habitaciones de un hotel."""

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    ROOM_TYPES = (
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
    )
    type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=15, decimal_places=0)
    capacity = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='room_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        """Meta options."""
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'

    def __str__(self):
        """Retorna la propiedad `number`."""
        return self.number


class Booking(models.Model):
    """Reservas de habitaciones."""

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    RESERVATION_STATUS = (
        ('approved', 'Aprobado'),
        ('outstanding', 'Pendiente'),
    )
    status = models.CharField(max_length=20, choices=RESERVATION_STATUS)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # TODO: esto debería ser un `IntegerField``
    additional_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        """Meta options."""
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
    
    def __str__(self):
        """Retorna la propiedad `username` del usuario."""
        return self.user.username
