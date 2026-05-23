from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Laptop
from .forms import LaptopForm

def laptop_list(request):
    query = request.GET.get('q', '') # берём параметр q из URL
    if query:
        laptops = Laptop.objects.filter(
            name__icontains=query # ищем по названию (без учёта регистра)
        ) | Laptop.objects.filter(
            brand__icontains=query # ищем по бренду (без учёта регистра)
        )
    else:
        laptops = Laptop.objects.all()
        
    return render(request, 'laptops/laptop_list.html', {
        'laptops': laptops,
        'query': query, # передаём текущий запрос в шаблон
    })

def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, 'laptops/laptop_detail.html', {'laptop': laptop})

def laptop_create(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laptop_list')
    else:
        form = LaptopForm()
    return render(request, 'laptops/laptop_create.html', {'form': form})

def laptop_update(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('laptop_list')
    else:
        form = LaptopForm(instance=laptop)
    return render(request, 'laptops/laptop_create.html', {'form': form})

def laptop_delete(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == 'POST':
        laptop.delete()
        return redirect('laptop_list')
    return render(request, 'laptops/laptop_delete.html', {'laptop': laptop})
# Create your views here.