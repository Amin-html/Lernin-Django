from django.urls import path
from . import views 

urlpatterns = [
    path('', views.phone_list, name='phone_list'),
    path('<int:pk>/', views.phone_detail, name='phone_detail'),
    path('create/', views.phone_create, name='phone_create'),
    path('<int:pk>/update/', views.phone_update, name='phone_update'),
    path('<int:pk>/delete/', views.phone_delete, name='phone_delete'),

    # API endpoints
    path('api/', views.PhoneListAPI.as_view(), name='phone_list_api'),
    path('api/<int:pk>/', views.PhoneDetailAPI.as_view(), name='phone_detail_api'),
]