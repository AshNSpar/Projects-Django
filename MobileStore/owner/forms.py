from django import forms

class Add_mobileForm(forms.Form):
    brand_name=forms.CharField()
    model_name=forms.CharField()
    price=forms.IntegerField()
    copies=forms.IntegerField()
    def clean(self):
        print("validate")

class RegForm(forms.Form):
    username=forms.CharField()
    email=forms.IntegerField()
    password=forms.CharField()
    cofirm_password=forms.CharField()
    def clean(self):
        print("validate")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    def clean(self):
        print("validate")