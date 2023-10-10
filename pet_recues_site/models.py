from django.db import models

class User (models.Model):
    user_name = models.CharField(verbose_name="Username", max_length=255)
    user_email = models.EmailField(verbose_name="Email", unique=True, primary_key=True)
    fisrt_name = models.CharField(verbose_name="First Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name", max_length=255)
    address = models.CharField(verbose_name="Address",max_length=255)
    suburb = models.CharField(verbose_name="Suburb", max_length=255)
    postcode = models.CharField(verbose_name="Postcode", max_length=10)
    DOB = models.DateField(verbose_name="Date of Birth")
    joined_date = models.DateField(verbose_name="Joined Date")

class Pet (models.Model):
    pet_name = models.CharField(verbose_name="Name", max_length=255)
    sex = models.CharField(verbose_name="Sex", max_length=10)
    species = models.CharField(verbose_name="Species", max_length=255)
    breed = models.CharField(verbose_name="Breed", max_length=255)
    health = models.TextField(verbose_name="Health Condition")
    location = models.CharField(verbose_name="Current Located")
    image = models.ImageField()




