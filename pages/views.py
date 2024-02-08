from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'is_home': True})
