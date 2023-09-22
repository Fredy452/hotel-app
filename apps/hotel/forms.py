# Django
from django import forms

# Models
from apps.hotel.models import Room, Amenity


class RoomForm(forms.ModelForm):
    amenities = forms.ModelMultipleChoiceField(
        queryset=Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Room
        fields = '__all__'
