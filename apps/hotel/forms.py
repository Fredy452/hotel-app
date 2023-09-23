"""Hotel forms."""

# Django
from django import forms

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
