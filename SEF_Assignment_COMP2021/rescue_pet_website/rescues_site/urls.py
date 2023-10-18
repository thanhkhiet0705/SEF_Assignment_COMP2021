from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('about_us/', views.about_us, name='about_us'),
    path('service/', views.service, name='service'),
    path('admin_user/', views.admin_user, name='admin_user'),
    path('pet_list/', views.pet_list, name='pet_list'),
]