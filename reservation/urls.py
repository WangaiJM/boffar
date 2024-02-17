from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.bookingView, name='bookings'),
]