from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    classNo = models.IntegerField()
    rollNo = models.IntegerField()
    FatherName = models.CharField(max_length=200)
    FatherNumber = models.IntegerField()

    def __str__(self):
        return self.name

