from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Menu

class menuAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu', 'price', 'active', 'registered_at']
    search_fields= ['title','registered_at']
    list_filter = ['active', 'registered_at']


admin.site.register(Menu, menuAdmin)