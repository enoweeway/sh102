import os
import random

from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 1239124123)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "users/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class UserQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(is_active=True)
    def featured(self):
        return self.filter(featured=True, is_active=True)

    def search(self, query):
        lookups = Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
        return self.filter(lookups).distinct()

class UserManager(models.Manager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)
    def all(self):
        return self.get_queryset().active()
    def featured(self):
        return self.get_queryset().featured()
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)




class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)

    mobile_number = models.CharField(max_length=11, null=True,blank=False, validators=[RegexValidator(r'^\d{10,11}$')])
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    USER_TYPE = (
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
        ('User', 'User')
    )
    userType = models. CharField(max_length=100, choices=USER_TYPE, blank=False, default='New')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    doctorPK = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
            return self.user.email

    def get_object():
        return get_object_or_404(UserProfile, user__username=self.kwargs['username'])

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=1000, blank=True)
    # avatar = models.TextField(blank = True)

    def __str__(self):
            return self.user.email

    def get_object():
        return get_object_or_404(UserProfile, user__username=self.kwargs['username'])