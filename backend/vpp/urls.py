# Path: backend/vpp/urls.py
    
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.member_dashboard, name='dashboard'),
]
