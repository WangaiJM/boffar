from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    menu_categories = [
        ('Mains', 'Mains'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
    ]
    category = models.CharField(max_length=100, choices=menu_categories)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Menu'