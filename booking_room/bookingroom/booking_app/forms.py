from django import forms

from .models import Booking


class Booking_form(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
