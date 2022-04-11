from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from employer.models import (JobseekerProfile,CompanyProfile,AbstractBaseUser,
                ApplicationModel,JobModel,MyUser,MyUserManager,BaseUserManager)


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Password Conformation",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = MyUser
        fields = ["email","phone","role","password1","password2"]

        widgets = {
        "email": forms.TextInput(attrs={"class": "form-control"}),
        "phone":  forms.NumberInput(attrs={"class": "form-control"}),
        "role": forms.Select(attrs={"class": "form-select"})
        }

class LogInForm(forms.Form):
    email=forms.CharField(widget = forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control"}))


class AddCompanyForm(ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ["company_name","company_description","logo"]


class AddJobForm(ModelForm):
    class Meta:
        model = JobModel
        fields = ["company","post_name","qualification","experience","description"]

class ApplicationForm(ModelForm):
    class Meta:
        model = ApplicationModel
        fields = ["job","application_status"]
        widgets={
            "job": forms.TextInput(attrs={"class": "form-control"}),
            "application_status": forms.Select(attrs={"class": "form-select"}),
        }