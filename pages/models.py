from django.db import models

class gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Galleries'
        
