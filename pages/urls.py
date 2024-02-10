from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.aboutView, name='about'),
    path('rooms/', views.roomsView, name='rooms'),
    path('teams/', views.teamView, name='team'),
    path('gallery/', views.galleryView, name='gallery'),
    path('contacts/', views.contactsView, name='contacts'),
]