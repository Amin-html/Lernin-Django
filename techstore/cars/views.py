from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Car
from .forms import CarForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CarSerializer

class CarListAPI(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CarDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def car_list(request):
    query = request.GET.get('q', '') # берём параметр q из URL
    if query:
        cars = Car.objects.filter(
            name__icontains=query # ищем по названию (без учёта регистра)
        ) | Car.objects.filter(
            brand__icontains=query # ищем по бренду (без учёта регистра)
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

@login_required # ⬅️ защита от неавторизованных пользователей
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/car_create.html', {'form': form})

@login_required # ⬅️ защита от неавторизованных пользователей
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_create.html', {'form': form})

@login_required # ⬅️ защита от неавторизованных пользователей
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_delete.html', {'car': car})
# Create your views here.
