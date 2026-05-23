from django.shortcuts import render
from django.http import HttpResponse

def laptop_list(request):
    laptops = [
        {'name': 'MacBook Pro', 'price': 1299},
        {'name': 'Dell XPS 13', 'price': 999},
        {'name': 'Lenovo ThinkPad X1 Carbon', 'price': 1499},
    ]
    return render(request, 'laptops/laptop_list.html', {'laptops': laptops})

# Create your views here.
