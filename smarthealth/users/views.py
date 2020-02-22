from django.contrib.auth import login
from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm, CustomUserCreationForm


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


def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.email = request.POST['email']
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})