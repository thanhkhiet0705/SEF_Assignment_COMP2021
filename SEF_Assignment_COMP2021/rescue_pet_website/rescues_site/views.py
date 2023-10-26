from django.shortcuts import render, redirect
from django.db import transaction
from .models import CustomUser, Pet, Application
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session

def home(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets
    }
    return render(request, 'rescues_site/home_page.html', context)

# @login_required
def user_home(request):
    if request.method == 'POST':
        username = request.session.get('username')
        print(username)
        context = {
            'username': username
        }
        return render(request, 'rescues_site/home_page.html', context)

def about_us(request):
    return render(request, 'rescues_site/about_us.html')

def service(request):
    return render(request, 'rescues_site/service.html')

def pet_list(request):
    return render(request, 'rescues_site/pet_list.html')

def admin_user(request):
    return render(request, 'rescues_site/admin_user.html')

def registration_form(request):
    return render(request, 'registration/sign_up.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user  = authenticate(request, username = username, password = password)
        if user is not None and user.is_active:
            login(request, user)
            request.session['username'] = user.username
            print(request.session['username'])
            return redirect('user_home')
        else:
            return render(request, 'registration/login.html')

@transaction.atomic
def sign_up(request):
    if request.method == 'GET':
        return render(request, 'registration/sign_up.html')
    
    if request.method == 'POST':
        error = []

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        suburb = request.POST.get('suburb')
        postcode = request.POST.get('postcode')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number', None)
        password = make_password(request.POST.get('password'))

        try:
            user = CustomUser.objects.create(username = email, 
                                             first_name = first_name, 
                                             last_name = last_name,
                                             address = address,
                                             suburb = suburb,
                                             postcode = postcode,
                                             phone_number = phone_number, 
                                             password = password)
            request.session['username'] = user.username
            return redirect('user_home')
        except Exception as e:
            error.append(str(e))
            print(f"User creation failed: {e}")
            return render(request, 'registration/sign_up.html', {'error': error})
        
def logout(request):
    request.session.clear()
    return redirect('home')