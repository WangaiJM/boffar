from django.shortcuts import render
from .models import gallery

def index(request):
    return render(request, 'index.html', {'is_home': True})

def aboutView(request):
    return render(request, 'about/about.html', {'title': 'About Us'})

def roomsView(request):
    return render(request, 'rooms/index.html', { 'title': 'Rooms'})

def teamView(request):
    return render(request, 'team/index.html', { 'title': 'team'})

def activitiesView(request):
    return render(request, 'activities/events.html', {'title': 'Activities'})


def galleryView(request):
    galleries = gallery.objects.all().order_by('-uploaded_at')
    context = {'galleries': galleries, 'title': 'Gallery'}
    return render(request, 'gallery/index.html', context)





