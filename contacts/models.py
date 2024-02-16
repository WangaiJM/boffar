from django.db import models

class contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    queried_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email