from django.contrib import admin
from .models import UserProfile, Pet, Application

admin.site.register(UserProfile)
admin.site.register(Pet)
admin.site.register(Application)
