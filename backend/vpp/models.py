from django.db import models
from django.contrib.auth.models import User  # Assuming user authentication

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    location = models.CharField(max_length=100)
    # ... other member related fields

class Device(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=50, choices=[
        ('BATTERY', 'Battery'), 
        ('SOLAR', 'Solar Panel'),
        ('EV', 'Electric Vehicle'), 
        ('SMART_APPLIANCE', 'Smart Appliance')
    ])
    capacity = models.FloatField()
    current_state = models.FloatField(default=0)  # Current charge or energy output
    # ... other device-specific fields

class EnergyData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    energy_value = models.FloatField()  # Energy produced, consumed, etc.
    # ... other energy data related fields


### API Endpoints (Outlined)
# Path: backend/vpp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.member_dashboard, name='dashboard'),
    path('api/member/', views.MemberList.as_view(), name='member-list'),
    path('api/member/<int:pk>/', views.MemberDetail.as_view(), name='member-detail'),
    path('api/device/', views.DeviceList.as_view(), name='device-list'),
    path('api/device/<int:pk>/', views.DeviceDetail.as_view(), name='device-detail'),
    path('api/energydata/', views.EnergyDataList.as_view(), name='energydata-list'),
    path('api/energydata/<int:pk>/', views.EnergyDataDetail.as_view(), name='energydata-detail'),
]
