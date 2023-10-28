from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from .models import UserProfile, Pet, Application
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
import sys
from django.http import HttpResponse
def home(request):
    if request.method == 'GET':
        pets = Pet.objects.all()
        context = {
            'pets': pets
        }
        return render(request, 'rescues_site/home_page.html', context)
    if request.method == 'POST':
        user = request.session.get('username')
        if user.is_authenticated:
            pets = Pet.objects.all()
            context = {
                'pets': pets,
                'user': user
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

def pet_detail(request):
    if request.method == "POST":
        pet_id = request.POST.get('pet_id')
        pet = Pet.objects.get(pet_id = pet_id)
        return render(request, 'rescues_site/pet_detail.html', context={'pet' : pet})
    
def pets(request):
    if request.method == "GET":
            pets = Pet.objects.all()
            context = {
                'pets': pets
            }
            return render(request, 'rescues_site/pets.html', context)

    if request.method == 'POST':
        selected_type = request.POST.get('selected_type')
        selected_type_value = request.POST.get('selected_type_value')
        selected_location = request.POST.get('selected_location')
        selected_location_value = request.POST.get('selected_location_value')

        ## If the type of pet is None
        if selected_type == '' and selected_type_value == '':
            if selected_location == 'state' and selected_location_value is not None:
                pets = Pet.objects.all()
                
                context = {
                    'pets': pets.filter(state__contains = selected_location_value)
                }
                return render(request, 'rescues_site/pets.html', context)
            
            elif selected_location == 'suburb' and selected_location_value is not None:
                pets = Pet.objects.all()
                
                context = {
                    'pets': pets.filter(suburb__contains = selected_location_value)
                }
                return render(request, 'rescues_site/pets.html', context)

        ## If the location of the pet is None  
        elif selected_location == '' and selected_location_value == '':
            if selected_type == 'species' and selected_type_value is not None:
                pets = Pet.objects.all()
                
                context = {
                    'pets': pets.filter(species__contains = selected_type_value)
                }
                return render(request, 'rescues_site/pets.html', context)
            
            elif selected_type == 'breed' and selected_type_value is not None:
                pets = Pet.objects.all()
                
                context = {
                    'pets': pets.filter(breed__contains = selected_type_value)
                }
                return render(request, 'rescues_site/pets.html', context)
            
            elif selected_type == 'gender' and selected_type_value is not None:
                pets = Pet.objects.all()
                male = 'male'
                female = 'female'
                if selected_type_value.lower() == male:
                    context = {
                        'pets': pets.filter(gender__contains = selected_type_value[0]).exclude(gender__contains = female)
                    }
                    return render(request, 'rescues_site/pets.html', context)
                
                if selected_type_value.lower() == female:
                    context = {
                        'pets': pets.filter(gender__contains = selected_type_value[0]).exclude(gender__iexact = male)
                    }
                    return render(request, 'rescues_site/pets.html', context)
                
            elif selected_type == 'age' and selected_type_value is not None:
                context = {
                    'pet': Pet.objects.filter(age = selected_type_value)
                }

                return render(request, 'rescues_site/pets.html', context)
        
        ## If all of the value is not None
        elif [selected_type, selected_type_value, selected_location, selected_location_value] is not None:
            #If the location type is State
            if selected_location == 'state' and selected_location_value is not None and selected_type == 'species' and selected_type_value is not None:
                pets = Pet.objects.all()
                
                context = {
                    'pets': pets.filter(state__contains = selected_location_value, species__contains = selected_type_value)
                }
                return render(request, 'rescues_site/pets.html', context)
            
            elif selected_location == 'state' and selected_location_value is not None and selected_type == 'breed' and selected_type_value is not None:
                pets = Pet.objects.all()
                
                context = {
                    'pets': pets.filter(state__contains = selected_location_value, breed__contains = selected_type_value)
                }
                return render(request, 'rescues_site/pets.html', context)
            
            elif selected_location == 'state' and selected_location_value is not None and selected_type == 'gender' and selected_type_value is not None:
                pets = Pet.objects.all()
                male = 'male'
                female = 'female'
                if selected_type_value.lower() == male:
                    context = {
                        'pets': pets.filter(state__contains = selected_location_value, gender__contains = selected_type_value[0]).exclude(gender__contains = female)
                    }
                    return render(request, 'rescues_site/pets.html', context)
                
                if selected_type_value.lower() == female:
                    context = {
                        'pets': pets.filter(state__contains = selected_location_value, gender__contains = selected_type_value[0]).exclude(gender__iexact = male)
                    }
                    return render(request, 'rescues_site/pets.html', context)
                
            elif selected_location == 'state' and selected_location_value is not None and selected_type == 'age' and selected_type_value is not None:
                context = {
                    'pet': Pet.objects.filter(state__contains = selected_location_value, age = selected_type_value)
                }

                return render(request, 'rescues_site/pets.html', context)
            
            # If the location type is Surburb
            if selected_location == 'suburb' and selected_location_value is not None and selected_type == 'species' and selected_type_value is not None:
                pets = Pet.objects.all()
                
                context = {
                    'pets': pets.filter(suburb__contains = selected_location_value, species__contains = selected_type_value)
                }
                return render(request, 'rescues_site/pets.html', context)
            
            elif selected_location == 'suburb' and selected_location_value is not None and selected_type == 'breed' and selected_type_value is not None:
                pets = Pet.objects.all()
                
                context = {
                    'pets': pets.filter(suburb__contains = selected_location_value, breed__contains = selected_type_value)
                }
                return render(request, 'rescues_site/pets.html', context)
            
            elif selected_location == 'suburb' and selected_location_value is not None and selected_type == 'gender' and selected_type_value is not None:
                pets = Pet.objects.all()
                male = 'male'
                female = 'female'
                if selected_type_value.lower() == male:
                    context = {
                        'pets': pets.filter(suburb__contains = selected_location_value, gender__contains = selected_type_value[0]).exclude(gender__contains = female)
                    }
                    return render(request, 'rescues_site/pets.html', context)
                
                if selected_type_value.lower() == female:
                    context = {
                        'pets': pets.filter(suburb__contains = selected_location_value, gender__contains = selected_type_value[0]).exclude(gender__iexact = male)
                    }
                    return render(request, 'rescues_site/pets.html', context)
                
            elif selected_location == 'suburb' and selected_location_value is not None and selected_type == 'age' and selected_type_value is not None:
                context = {
                    'pet': Pet.objects.filter(suburb__contains = selected_location_value, age = selected_type_value)
                }

                return render(request, 'rescues_site/pets.html', context)
            
    else:
        pets = Pet.objects.all()
        context = {
            'pets': pets
        }
        return render(request, 'rescues_site/pets.html', context)

def login_page(request):
    return render(request, 'registration/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user  =  authenticate(username = username, password = password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')

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
            user = User.objects.create_user(username = email, 
                                             first_name = first_name, 
                                             last_name = last_name,
                                             password = password)
            
        except Exception as e:
            pass
        
        new_user = UserProfile(address = address,
                                suburb = suburb,
                                postcode =postcode,
                                phone_number = phone_number)
        
        try:
            new_user.save()
        except:
            pass

        login(request)
        return redirect('home')

def logout(request):
    request.session.clear()
    return redirect('home')