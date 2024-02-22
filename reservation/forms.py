from django import forms
from django.conf import settings
from django.forms import ModelForm, DateInput
from .models import Reservation  # Assuming your model is named Contact with capital 'C'

class bookingForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
        widgets = {
            'check_in_date': DateInput(format=settings.DATETIME_FORMAT, attrs={"class": "datepicker"}),
            'check_out_date': DateInput(format=settings.DATETIME_FORMAT, attrs={'class': 'datepicker'})  
        }
