from django.db import models

class User (models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(unique=True, primary_key=True)
    fisrt_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    DOB = models.DateField()
    joined_date = models.DateField()




