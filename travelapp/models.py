from django.db import models


# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()

    # dest = models.CharField(max_length=20,default='null')
    # OPTION_ONE = 'dest 1'
    # OPTION_TWO = 'dest 2'
    # OPTION_THREE = 'dest 3'
    #
    # CHOICES = [
    #     (OPTION_ONE, 'Option 1'),
    #     (OPTION_TWO, 'Option 2'),
    #     (OPTION_THREE, 'Option 3'),
    # ]
    # dest = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.name
