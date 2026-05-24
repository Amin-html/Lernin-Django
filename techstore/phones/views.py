from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Phone
from .forms import PhoneForm

def phone_list(request):
    query = request.GET.get('q', '') # берём параметр q из URL
    if query:
        phones = Phone.objects.filter(
            name__icontains=query # ищем по названию (без учёта регистра)
        ) | Phone.objects.filter(
            brand__icontains=query # ищем по бренду (без учёта регистра)
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

@login_required # ⬅️ защита от неавторизованных пользователей
def phone_create(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phone_list')
    else:
        form = PhoneForm()
    return render(request, 'phones/phone_create.html', {'form': form})

@login_required # ⬅️ защита от неавторизованных пользователей
def phone_update(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        form = PhoneForm(request.POST, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone_list')
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'phones/phone_create.html', {'form': form})

@login_required # ⬅️ защита от неавторизованных пользователей
def phone_delete(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone_list')
    return render(request, 'phones/phone_delete.html', {'phone': phone})
# Create your views here.