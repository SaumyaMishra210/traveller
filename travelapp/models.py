from django.db import models
# Create your models here.
class Bookingmodel(models.Model):
    departDate = models.DateField(max_length=10, default='00-00-0000')
    returnDate = models.DateField(max_length=10, default='00-00-0000')
    BOOKING_DESTINATION = [
        ('Destination', 'Destination'),
        ('Destination1', 'Goa'),
        ('Destination2', 'Mumbai'),
        ('Destination3', 'Laddakh'),
    ]
    destination = models.CharField(max_length=15, choices=BOOKING_DESTINATION, default='Destination')
    BOOKING_DURATION = [
        ('Duration', 'Duration'),
        ('Duration1', 'month 1'),
        ('Duration2', 'month 2'),
        ('Duration3', 'month 3'),
    ]
    duration = models.CharField(max_length=20, choices=BOOKING_DURATION, default='Duration')
    def __str__(self):
        return f"{self.duration} - {self.destination}"


class SignUpmodel(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    BOOKING_DESTINATION = [
        ('Destination', 'Destination'),
        ('Destination1', 'Goa'),
        ('Destination2', 'Mumbai'),
        ('Destination3', 'Laddakh'),
    ]
    destination = models.CharField(max_length=15, choices=BOOKING_DESTINATION, default='Destination')

    def __str__(self):
        return self.name
