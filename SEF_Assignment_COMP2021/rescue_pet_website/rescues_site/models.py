from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, null=True)
    address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    reference = models.CharField(max_length=2500, null=True, blank=True)

class Pet(models.Model):
    name = models.CharField(max_length=255, null=False)
    species = models.CharField(max_length=255, null= False)
    breed = models.CharField(max_length=255, null=True)
    age = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    image_path = models.TextField(null=True)
    status  = models.CharField(max_length=255,null=False)
    suburb = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    fee = models.BigIntegerField()
    date_added = models.DateField()

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    app_ref = models.TextField(max_length=5000, null=False)