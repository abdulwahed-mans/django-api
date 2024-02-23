from django.shortcuts import redirect, render
from .models import Member, Device

def member_dashboard(request):
    if request.user.is_authenticated:
        member = Member.objects.get(user=request.user)
        devices = Device.objects.filter(member=member)
        context = {'member': member, 'devices': devices}
        return render(request, 'vpp/dashboard.html', context)
    else:
        return redirect('/')
    # return redirect('/admin/login/?next=/vpp/dashboard/')  # Redirect to admin login page if user is not authenticated
