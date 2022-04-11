from django.forms import ModelForm
from reporting.models import MyUser,Course,Batch,Timesheet
from reporting.admin import UserCreationForm
from django import forms

class AddUserForm(UserCreationForm):
    password1 = forms.CharField(label = "Password" ,widget = forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(label = "Password Conformation", widget = forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=MyUser
        fields=["email","role","password1","password2"]
        widgets={
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "role": forms.Select(attrs={"class":"form-select"})
        }

class AddCourseForm(ModelForm):
    class Meta:
        model=Course
        fields=["course_name"]

class AddBatchForm(ModelForm):
    class Meta:
        model=Batch
        fields=["course","batch_name"]

class SignInForm(forms.Form):
    email=forms.CharField(widget = forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget = forms.PasswordInput(attrs={"class":"form-control"}))

class TimesheetForm(ModelForm):
    class Meta:
        model = Timesheet
        fields = ["batch","topic","topic_status"]
        widgets={
            "batch":forms.Select(attrs={"class":"form-select"}),
            "topic": forms.TextInput(attrs={"class": "form-control"}),
            "topic_status": forms.Select(attrs={"class": "form-select"})
        }

