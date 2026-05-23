from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('<int:pk>/', views.car_detail, name='car_detail'),
    path('create/', views.laptop_create, name='car_create'),
]