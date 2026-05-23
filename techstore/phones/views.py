from django.shortcuts import render
from django.http import HttpResponse

def phone_list(request):
    phones = [
        {'name': 'iPhone 13', 'price': 799},
        {'name': 'Samsung Galaxy S21', 'price': 699},
        {'name': 'Google Pixel 6', 'price': 599},
    ]
    return render(request, 'phones/phone_list.html', {'phones': phones})
# Create your views here.
