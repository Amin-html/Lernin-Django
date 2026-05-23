from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Phone

def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phones/phone_list.html', {'phones': phones})

def phone_detail(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    return render(request, 'phones/phone_detail.html', {'phone': phone})
# Create your views here.
