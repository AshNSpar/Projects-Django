from django.shortcuts import render
from customer import forms

# Create your views here.
def signup_view(request):
    form = forms.UserCreationForm()
    context = {}
    context["form"] = form

    return render(request, "customer/signup.html", context)