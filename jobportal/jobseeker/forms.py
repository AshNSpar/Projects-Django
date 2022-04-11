from django import forms
from employer.models import JobseekerProfile,ApplicationModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfile
        fields = ["profile_picture","name","skill","resume"]
        widgets ={
            "profile_picture": forms.FileInput(attrs = {"class" : "form-control"}),
            "name": forms.TextInput(attrs = {"class" : "form-control"}),
            "skill": forms.TextInput(attrs = {"class" : "form-control"}),
            "resume": forms.FileInput(attrs = {"class": "form-control"}),
        }