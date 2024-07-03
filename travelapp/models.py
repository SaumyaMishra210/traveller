from django.db import models

# Create your models here.
class Bookingmodel(models.Model):
    departDate = models.DateField(max_length=10,default='None')
    returnDate = models.DateField(max_length=10,default='None')
    BOOKING_DESTINATION = [
        ('', 'Destination'),
        ('Destination1', 'Goa'),
        ('Destination2', 'Mumbai'),
        ('Destination3', 'Laddakh'),
    ]
    destination = models.CharField(max_length=15, choices=BOOKING_DESTINATION,default='Destination')

    BOOKING_DURATION = [
        ('', 'Duration'),
        ('Duration1', 'Duration1'),
        ('Duration2', 'Duration2'),
        ('Duration3', 'Duration3'),
    ]
    duration = models.CharField(max_length=20,choices=BOOKING_DURATION,default='Duration')


class SignUpmodel(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return self.name
