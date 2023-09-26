"""Hotel forms."""

# Django
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

# Models
from apps.hotel.models import Room, Amenity


class RoomForm(forms.ModelForm):
    """Room model form."""

    amenities = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Comodidades',
    )

    class Meta:
        model = Room
        fields = '__all__'


class ReservationForm(forms.Form):
    check_in_date = forms.DateField(
        widget=DatePickerInput(
            format='%Y-%m-%d',
            options={
                "startDate": "today",  # Establece la fecha mínima como hoy
                "autoclose": True,
            }
        ),  # Especifica el formato de fecha deseado
    )
    check_out_date = forms.DateField(
        widget=DatePickerInput(
            format='%Y-%m-%d',
            options={
                "startDate": "today",  # Establece la fecha mínima como hoy
                "autoclose": True,
            }
        )
    )

