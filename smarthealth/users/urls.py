from django.urls import path

from users.views import DoctorListView, PatientListView
from . import views
from django.conf.urls import url
app_name = 'users'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    # path('doctors/', views.DoctorListView, name='doctorList'),
    url(r'^doctors/', DoctorListView.as_view(), name='doctorList'),
    url(r'^patients/', PatientListView.as_view(), name='patientList'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', views.get_user_profile, name='profile'),
    path('signup/', views.SignUp, name='signup'),
]