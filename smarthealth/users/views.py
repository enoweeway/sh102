from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm


def login_page(request):
    form = LoginForm(request.POST or None)

    # print(request.user.is_authenticated)
    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:
            login(request, user)
            # success_url = reverse_lazy('login')
            # ontext['form'] = LoginForm()
            return redirect('dashboard')
    context = {
        "form": form
    }

    return render(request, "auth/login.html", context)