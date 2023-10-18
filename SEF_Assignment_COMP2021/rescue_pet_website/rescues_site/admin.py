from django.contrib import admin
from .models import CustomUser, Pet, Application

admin.site.register(CustomUser)
admin.site.register(Pet)
admin.site.register(Application)
