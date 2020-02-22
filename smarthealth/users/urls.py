from django.urls import path

from . import views
from django.conf.urls import url
app_name = 'users'

urlpatterns = [
    path('login/', views.login_page, name='login'),
]