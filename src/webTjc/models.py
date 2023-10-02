from django.db import models
from django_countries.fields import CountryField


# Create your models here.


class Merch(models.Model):
    name = models.CharField(max_length=100)
    product_image = models.ImageField()
    product_price = models.IntegerField()
    product_description = models.TextField(max_length=500)


    def __str__(self):
        return self.name
    

class AboutImages(models.Model):
    image = models.ImageField()


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    country = CountryField(multiple=False)

    def __str__(self):
        return self.first_name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    your_email = models.EmailField()
    message_body = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
    