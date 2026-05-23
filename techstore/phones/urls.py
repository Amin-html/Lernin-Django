from django.urls import path
from . import views 

urlpatterns = [
    path('', views.phone_list, name='phone_list'),
    path('<int:pk>/', views.phone_detail, name='phone_detail'),
    path('create/', views.phone_create, name='phone_create'),
]