from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from .models import CustomUser, User

pets = [
    {
        'name': 'Bim',
        'species': 'Dog',
        'sex': 'Male',
    },
    {
        'name': 'Choco',
        'species': 'Dog',
        'sex': 'Female',
    },
    {
        'name': 'Vani',
        'species': 'Dog',
        'sex': 'Female',
    }
]

def home(request):
    context = {
        'pets': pets
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

@transaction.atomic
def sign_up(request):

    if request.method == 'POST':
        error = []

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        suburb = request.POST.get('suburb')
        postcode = request.POST.get('postcode')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number', None)
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username = email, 
                                             first_name = first_name, 
                                             last_name = last_name, 
                                             password = password)
        
        except Exception as e:
            error.append(str(e))
            print(f"User creation failed: {e}")
            return render(request, 'registration/sign_up.html', {'error': error})
        
        new_user = CustomUser(
            address = address,
            suburb = suburb,
            postcode = postcode,
            phone_number = phone_number
        )
        
        try:
            new_user.save()
        except Exception as e:
            error.append(str(e))
            print(f"User creation failed: {e}")
            return render(request, 'registration/sign_up.html', {'error': error})
        
    return redirect('home_page')
