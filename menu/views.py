from django.shortcuts import render
from .models import Menu

def menuView(request):
    menus = Menu.objects.all()
    context = {'menus': menus}
    return render(request, 'menus/index.html', context)

def homeMenu(request):
    menus = Menu.objects.all()
    context = {'home_menu': menus}
    return render(request, 'index.html', context)