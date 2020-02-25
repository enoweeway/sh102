from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from users.backend import EmailOrUsernameModelBackend

# Create your views here.
from users.models import UserProfile, CustomUser
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.hashers import make_password


def login_page(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:

            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
    context = {
        "form": form
    }

    return render(request, "auth/login.html", context)


def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            hashed = make_password(request.POST['password2'])
            obj = CustomUser.objects.create(username=request.POST['username'],
                                                 email=request.POST['email'],
                                                 password=hashed,
                                                 userType=request.POST['userType'],
                                                 mobile_number=request.POST['mobile_number'],
                                                 first_name=request.POST['first_name'],
                                                 last_name=request.POST['last_name'],
                                                 doctorPK=request.POST['doctorPK'],
                                                 gender=request.POST['gender']
                                                 )
            obj.save()
            if request.user.is_authenticated:
                return redirect('dashboard')
            else:
                return render(request, 'auth/error.html', {})
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})





class DoctorListView(ListView):
    template_name = "users/list_doctor.html"
    def get_queryset(self, *args, **kwargs):
        doctor = CustomUser.objects.filter(userType="Doctor")
        context = {
            'doctor': doctor
        }
        return context

class PatientListView(ListView):
    template_name = "users/list_patient.html"
    def get_queryset(self, *args, **kwargs):

        patient = CustomUser.objects.filter(userType="Patient")
        context = {
            'patient': patient
        }
        return context

def edit_profile(request, username):
    if request.user.is_superuser:
        user = CustomUser.objects.get(username=username)
    else:
        user = CustomUser.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        # print(request.user.is_authenticated())
        if form.is_valid():
            # form.middle_name = request.POST['middle_name']
            # form.profile_image = request.FILES.get('profile_image', user.profile_image)
            form.save()
            return redirect('users:profile', user)
    else:
        form = CustomUserChangeForm(instance=user)
        args = {
            'form': form,
            'user': user
            }
        if user.username == request.user.username or request.user.is_superuser:
            return render(request, 'users/edit_profile.html', args)
        else:
            return render(request, 'auth/error.html', {})

class user_profile(ListView):
    model = UserProfile
    count_hit = True
    template_name = 'users/profile.html'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)

def get_user_profile(request, username):
    user = CustomUser.objects.get(username=username)
    if request.user.username == user.username or request.user.is_superuser:
        return render(request, 'users/profile.html', {"user":user})
    else:
        return render(request, 'auth/error.html', {})
