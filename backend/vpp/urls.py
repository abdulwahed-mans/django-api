# Path: backend/vpp/urls.py
    
from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_dashboard, name='dashboard'),
]
