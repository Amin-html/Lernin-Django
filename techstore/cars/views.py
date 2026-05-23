from django.shortcuts import render
from django.http import HttpResponse

def car_list(request):
    cars = [
        {'name': 'Toyota Camry', 'price': 24000},
        {'name': 'Honda Accord', 'price': 22000},
        {'name': 'Ford Mustang', 'price': 26000},
    ]
    return render(request, 'cars/car_list.html', {'cars': cars})
# Create your views here.
