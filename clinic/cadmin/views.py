from django.shortcuts import render,redirect
from cadmin import forms
from cadmin import models

# Create your views here.
def DoctorCreate_view(request):
    if request.method=="GET":
        form=forms.DoctorAddForm()
        context={}
        context["form"]=form
        return  render(request,"doctoradd.html",context)
    elif request.method == "POST":
        form=forms.DoctorAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doctorlist")
        else:
            return render(request,'doctoradd.html',{"form":form})

def DoctorList_view(request):
    form=forms.DoctorSearchForm()
    doctors=models.Doctor.objects.all()
    context={}
    context["form"]=form
    context["doctors"]=doctors
    if request.method=="POST":
            form=forms.DoctorSearchForm(request.POST)
            if form.is_valid():
                doctor_name=form.cleaned_data["doctor_name"]
                doctors=models.Doctor.objects.filter(doctor_name__contains=doctor_name)
                context["doctors"]=doctors
                return render(request,"doctorlist.html",context)
    return render(request,"doctorlist.html",context)

def DoctorRemove_view(request,id):
    doctor =models.Doctor.objects.get(id=id)
    doctor.delete()
    return redirect("doctorlist")

def DoctorDetails_view(request,id):
    doctor=models.Doctor.objects.get(id=id)
    context={}
    context["doctor"]=doctor
    return redirect(request,"doctordetails.html",context)


def DoctorChange_view(request,id):
    doctor = models.Doctor.objects.get(id=id)
    form = forms.DoctorEditForm(instance=doctor)
    context={}
    context["form"] = form
    if request.method == "POST":
        form = forms.DoctorEditForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctorlist")
    return render(request,'doctorupdate.html',{"form": form})