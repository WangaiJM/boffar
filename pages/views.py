from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'is_home': True})

def aboutView(request):
    return render(request, 'about/about.html', {'is_home': False, 'title': 'About Us'})
