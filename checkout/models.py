from django.db import models
from products.models import Product
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Order(models.Model):
    # Model for user's order
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, editable=False, related_name='orders', verbose_name="Your username:")
    full_name = models.CharField(max_length=50, blank=False, verbose_name="Your full name:")
    phone_number = models.CharField(max_length=20, blank=False, verbose_name="Your phone number:")
    country = CountryField(blank_label='Where do you live?', null=True, blank=True, verbose_name="Country:")
    postcode = models.CharField(max_length=20, blank=True, verbose_name="Post code:")
    town_or_city = models.CharField(max_length=40, blank=False, verbose_name="Town or city:")
    street_address1 = models.CharField(max_length=40, blank=False, verbose_name="Address (Line 1):")
    street_address2 = models.CharField(max_length=40, blank=False, verbose_name="Address (Line 2):")
    county = models.CharField(max_length=40, blank=True, verbose_name="County:")
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class OrderLineItem(models.Model):
    # Information for items in user's order
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)
