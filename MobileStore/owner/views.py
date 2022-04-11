from django.shortcuts import render
from owner.forms import  Add_mobileForm,RegForm,LoginForm
# Create your views here.

def add_mobile(request):
    if request.method == "GET":
      form=Add_mobileForm()
      context={}
      context["form"]=form
      return render(request,"addmobile.html",context)
    elif request.method=="POST":
        form = Add_mobileForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data["brand"]
            model = form.cleaned_data["model"]
            price = form.cleaned_data["price"]
            copies = form.cleaned_data["copies"]
            print(form.cleaned_data)
            return render(request,'addmobile.html',{"form":form})
        else:
            return render(request, 'addmobile.html', {"form": form})