from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Laptop

def laptop_list(request):
    query = request.GET.get('q', '') # берём параметр q из URL
    if query:
        laptops = Laptop.objects.filter(
            name__icontains=query # ищем по названию (без учёта регистра)
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
# Create your views here.
