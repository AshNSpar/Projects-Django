from django.shortcuts import render

from Maths.forms import CalculationForm
from Maths.forms import CubeForm


# Create your views here.

def cube_numbers(request):
    if request.method=="GET":
        form=CubeForm()
        context={}
        context["form"]=form
        return render(request,"cube.html",context)
    elif request.method=="POST":
        form=CubeForm(request.POST)
        if form.is_valid():
            num=form.cleaned_data["num"]
            res=num**2
            context={}
            context["result"]=res
            return render(request,"cube.html",context)
        else:
            return render(request, "cube.html",{"form":form})
    return render(request,"cube.html")

def add_numbers(request):
    if request.method=="GET":
        form=CalculationForm()
        context={}
        context["form"]=form
        return render(request,"addition.html",context)
    elif request.method=="POST":
        form=CalculationForm(request.POST)
        if form.is_valid():
          num1=form.cleaned_data["num1"]
          num2=form.cleaned_data["num2"]
          res=num1+num2
          context={}
          context["result"]=res
          return render(request, "addition.html",context)
        else:
            return render(request, "addition.html",{"form":form})
    return render(request,"addition.html")

def sub_numbers(request):
    if request.method=="GET":
        form=CalculationForm()
        context={}
        context["form"]=form
        return render(request, "subtraction.html",context)
    elif request.method=="POST":
        form = CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            res = num1 - num2
            context = {}
            context["result"] = res
            return render(request, "subtraction.html",context)
        else:
            return render(request, "subtraction.html",{"form":form})
    return render(request, "subtraction.html")

def mult_numbers(request):
    if request.method=="GET":
        form=CalculationForm()
        context={}
        context["form"]=form
        return render(request, "multiplication.html",context)
    elif request.method=="POST":
        form = CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            res = num1 * num2
            context = {}
            context["result"] = res
            return render(request, "multiplication.html",context)
        else:
            return render(request, "multiplication.html",{"form":form})
    return render(request, "multiplication.html")

def div_numbers(request):
    if request.method=="GET":
        form=CalculationForm()
        context={}
        context["form"]=form
        return render(request, "division.html",context)
    elif request.method=="POST":
        form = CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data["num1"]
            num2 = form.cleaned_data["num2"]
            res = num1 / num2
            context = {}
            context["result"] = res
            return render(request, "division.html", context)
        else:
            return render(request, "division.html",{"form":form})
    return render(request, "division.html")

def index(request):
    return render(request,"index.html")