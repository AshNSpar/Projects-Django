from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from cadmin.models import Appointment

class AppoinmentForm(ModelForm):
    class Meta:
        model=Appointment
        fields=["patient_name","patient_gender", "patient_phno","appointment_date","appointment_time"]
        labels={
            "patient_name":"Name","patient_gender":"Gender","patient_phno":"Phone Number","appointment_date":"Booking Date","appointment_time":"Booking Time"
        }

class UserRegistrationForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:

      model = User
      fields = ["first_name","username","email"]
      widgets = {
          "first_name":forms.TextInput(attrs={"class":"form-control"}),
          "username":forms.TextInput(attrs={"class":"form-control"}),
          "email":forms.EmailInput(attrs={"class":"form-control"})
      }

class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))