from django.db import models

class Reservation(models.Model):
    firstname = models.CharField(max_length = 150)
    lastname = models.CharField(max_length = 150)
    contact = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booked_at = models.DateTimeField(auto_now_add=True)