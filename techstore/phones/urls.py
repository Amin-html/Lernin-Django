from django.urls import path
from . import views 

urlpatterns = [
    path('', views.phone_list, name='phone_list'),
]