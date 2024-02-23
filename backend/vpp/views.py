from django.shortcuts import render
from .models import Device


def member_dashboard(request):
   
    context = {}
    
    return render(request, 'vpp/dashboard.html', context)