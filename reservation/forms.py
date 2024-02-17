from django.forms import ModelForm
from .models import Reservation

class bookingForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"