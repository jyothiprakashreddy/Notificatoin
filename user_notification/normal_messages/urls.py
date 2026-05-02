from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.user_notifications, name='notifications'),
    path('appointment/', views.appointment_view, name='appointment')
    
    ]