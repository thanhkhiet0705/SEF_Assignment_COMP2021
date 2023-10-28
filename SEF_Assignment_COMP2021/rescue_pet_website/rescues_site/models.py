from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14, null=True)
    address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    reference = models.CharField(max_length=2500, null=True, blank=True)

class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=255, choices=[('Male', 'Male'), ('Female', 'Female'), ('Unsex', 'Unsex')])
    description = models.TextField()
    image_path = models.TextField(null=True)
    status  = models.CharField(max_length=255, choices=[('Available','Available'), ('Adopted','Adopted'), ('Pending', 'Pending')])
    suburb = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, choices=[('NSW','NSW'), ('QLD','QLD'), ('VIC','VIC'), ('ACT','ACT'), ('TAS','TAS'), ('NT','NT'), ('SA','SA'), ('WA','WA')])
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    application_status = models.CharField(max_length=10, choices=[('Pending','Pending'), ('Approve', 'Approve'), ('Decline', 'Decline')])
    application_note = models.TextField()
    adoption_date = models.DateTimeField(null=True)