from django.urls import path
from . import views

urlpatterns = [
    path('', views.laptop_list, name='laptop_list'),
    path('<int:pk>/', views.laptop_detail, name='laptop_detail'),
    path('create/', views.laptop_create, name='laptop_create'),
    path('<int:pk>/update/', views.laptop_update, name='laptop_update'),
    path('<int:pk>/delete/', views.laptop_delete, name='laptop_delete'),

    # API endpoints
    path('api/', views.LaptopListAPI.as_view(), name='laptop_list_api'),
    path('api/<int:pk>/', views.LaptopDetailAPI.as_view(), name='laptop_detail_api'),
]