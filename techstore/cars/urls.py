from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('<int:pk>/', views.car_detail, name='car_detail'),
    path('create/', views.car_create, name='car_create'),
    path('<int:pk>/update/', views.car_update, name='car_update'),
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),

    # API endpoints
    path('api/', views.CarListAPI.as_view(), name='car_list_api'),
    path('api/<int:pk>/', views.CarDetailAPI.as_view(), name='car_detail_api'),
]