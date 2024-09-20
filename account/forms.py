from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class createUserForm(UserCreationForm):
    class Meta:
        model = User
        field = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        

class createEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['phoneNumber', 'salary']


class editEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = ["phoneNumber", "salary"]

class editUser(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class editGuest(ModelForm):
    class Meta:
        model = Guest
        fields = ["phoneNumber"]


class ROLES(forms.Form):
    ROLES_TYPES = [ 
        ('manager', 'manager'),
        ('receptionist', 'receptionist'),
        ('staff', 'staff'),
    ]

    ROLES_TYPES = forms.CharField(widget=forms.RadioSelect(choices=ROLES_TYPES))