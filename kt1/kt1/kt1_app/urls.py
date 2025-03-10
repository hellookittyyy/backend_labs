from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_url, name='create_url'),
    path('delete/', views.delete_url, name='delete_url'),
    path('update/', views.update_url, name='update_url'),
    path('get/', views.get_url, name='get_url'),
    path('<str:shortCode>/', views.view_url, name='view_url'),
]