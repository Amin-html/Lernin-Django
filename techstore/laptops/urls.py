from django.urls import path
from . import views

urlpatterns = [
    path('', views.laptop_list, name='laptop_list'),
    path('<int:pk>/', views.laptop_detail, name='laptop_detail'),
]