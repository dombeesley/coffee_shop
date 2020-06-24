from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    town_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=40)
    street_address2 = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.email
