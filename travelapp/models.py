from django.db import models

# Create your models here.
class Booking(models.Model):
    depart_date = models.CharField(max_length=10)
    return_date = models.CharField(max_length=10)
    BOOKING_DESTINATION = [
        ('', 'Destination'),
        ('Destination1', 'Destination1'),
        ('Destination2', 'Destination2'),
        ('Destination3', 'Destination3'),
    ]
    destination = models.CharField(max_length=15, choices=BOOKING_DESTINATION)

    BOOKING_DURATION = [
        ('', 'Duration'),
        ('Duration1', 'Duration1'),
        ('Duration2', 'Duration2'),
        ('Duration3', 'Duration3'),
    ]
    duration = models.CharField(max_length=20,choices=BOOKING_DURATION)


class SignUp(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return self.name
