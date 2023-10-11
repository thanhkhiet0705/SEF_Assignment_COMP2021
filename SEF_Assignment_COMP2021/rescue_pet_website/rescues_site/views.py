from django.shortcuts import render
from django.http import HttpResponse

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
