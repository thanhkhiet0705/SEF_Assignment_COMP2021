from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_home', views.user_home, name='user_home'),
    path('about_us/', views.about_us, name='about_us'),
    path('service/', views.service, name='service'),
    path('admin_user/', views.admin_user, name='admin_user'),
    path('pet_list/', views.pet_list, name='pet_list'),
    path('login/', views.login_page, name='login_page'),
    path('login_user/', views.login, name='login_user'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('pets/', views.pets, name='pets'),
    path('pet_detail/', views.pet_detail, name='pet_detail'),
]