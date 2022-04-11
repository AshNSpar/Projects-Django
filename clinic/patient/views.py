from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from cadmin.models import Doctor
from patient import forms
from django.contrib import messages


# Create your views here.
def signup_view(request):
    form = forms.UserRegistrationForm()
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return redirect(request,"patient/signup.html",{"form":form})
    return render(request,"patient/signup.html", context)

def signin_view(request):
    form = forms.LoginForm()
    context = {}
    context['form'] = form

    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user:
                login(request, user)
                return redirect("userhome")
            else:
                messages.error(request, "invalid user detected")
                return redirect('signin')
    return render(request, 'patient/signin.html', context)

def userhome_view(request):
    return render(request,"patient/user_home.html")

def appoinment_view(request):
    form=forms.AppoinmentForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.AppoinmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userhome")
    return render(request,"patient/booking.html",context)