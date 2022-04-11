from django.forms import ModelForm
from django import forms
from cadmin.models import Doctor

class DoctorAddForm(ModelForm):

    class Meta:
        model=Doctor
        fields="__all__"

        widgets={
           "doctor_name":forms.TextInput(attrs={"class":"form-control"}),
           "department":forms.TextInput(attrs={"class":"form-control"}),
           "duty_time":forms.NumberInput(attrs={"class":"form-control"}),
           "fees":forms.NumberInput(attrs={"class":"form-control"})
        }
        labels={
        }

class DoctorEditForm(ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"


class DoctorRemoveForm(forms.Form):
    doctor_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    department=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    duty_time=forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))
    fees=forms.IntegerField(widget=forms.NumberInput(attrs={'class':"form-control"}))


class DoctorSearchForm(forms.Form):
    doctor_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","required":False}))

