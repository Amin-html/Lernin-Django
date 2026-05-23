from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car

def car_list(request):
    query = request.GET.get('q', '') # берём параметр q из URL
    if query:
        cars = Car.objects.filter(
            name__icontains=query # ищем по названию (без учёта регистра)
        )
    else:
        cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {
        'cars': cars,
        'query': query, # передаём текущий запрос в шаблон
        })

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})
# Create your views here.
