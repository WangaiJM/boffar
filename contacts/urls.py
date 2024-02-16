from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contactsView, name='contacts'),
]