from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from madmin.models import (MyUser,AddUser,AddDevice)


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Password Conformation",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = MyUser
        fields = ["email","role","password1","password2"]

        widgets = {
        "email": forms.TextInput(attrs={"class": "form-control"}),
        "role": forms.Select(attrs={"class": "form-select"})
        }

class LogInForm(forms.Form):
    email=forms.CharField(widget = forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control"}))


class AddDeviceForm(ModelForm):
    class Meta:
        model = AddDevice
        fields = ["imei_number","primary_sim","secondary_sim","firmware_option"]


class AddUserForm(ModelForm):
    class Meta:
        model = AddUser
        fields = ["user_name","address","dob"]

