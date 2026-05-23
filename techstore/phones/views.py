from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Phone

def phone_list(request):
    query = request.GET.get('q', '') # берём параметр q из URL
    if query:
        phones = Phone.objects.filter(
            name__icontains=query # ищем по названию (без учёта регистра)
        )
    else:
        phones = Phone.objects.all()
    return render(request, 'phones/phone_list.html', {
        'phones': phones,
        'query': query, # передаём текущий запрос в шаблон
    })

def phone_detail(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    return render(request, 'phones/phone_detail.html', {'phone': phone})
# Create your views here.
