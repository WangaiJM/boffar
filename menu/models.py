from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    menu_categories = [
        ('Mains', 'Mains'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
    ]
    menu = models.CharField(max_length=100, choices=menu_categories)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Menu'