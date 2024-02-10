from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'is_home': True})

def aboutView(request):
    return render(request, 'about/about.html', {'title': 'About Us'})

def roomsView(request):
    return render(request, 'rooms/index.html', { 'title': 'Rooms'})

def teamView(request):
    return render(request, 'team/index.html', { 'title': 'team'})

def galleryView(request):
    return render(request, 'gallery/index.html', { 'title': 'Gallery'})

def contactsView(request):
    return render(request, 'contacts/index.html', { 'title': 'Contact Us'})


