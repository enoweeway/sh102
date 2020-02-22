from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/views/dashboard.html', {})
    else:
        return redirect('users:login')


