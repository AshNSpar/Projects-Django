from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from reporting.models import MyUser,Course,Batch,Timesheet
from reporting import forms

# Create your views here.
class AdminHome(TemplateView):
        template_name = "reporting/admin_home.html"

class UserAdd(CreateView):
    model=MyUser
    form_class=forms.AddUserForm
    template_name = "reporting/user_add.html"
    success_url = reverse_lazy("adminhome")

class Users(ListView):
    model = MyUser
    template_name = "reporting/user_list.html"
    context_object_name = "users"

class UserEdit(UpdateView):
    model=MyUser
    template_name = "reporting/batch_edit.html"
    form_class= forms.AddUserForm
    pk_url_kwarg ="id"
    success_url = reverse_lazy("users")

class CourseAdd(CreateView):
    model=Course
    form_class=forms.AddCourseForm
    template_name = "reporting/course_add.html"
    success_url = reverse_lazy("adminhome")

class Courses(ListView):
    model=Course
    template_name = "reporting/course_list.html"
    context_object_name = "courses"

class CourseEdit(UpdateView):
    model=Course
    template_name = "reporting/batch_edit.html"
    form_class= forms.AddCourseForm
    pk_url_kwarg ="id"
    success_url = reverse_lazy("courses")

class BatchAdd(CreateView):
    model=Batch
    template_name = "reporting/batch_add.html"
    form_class=forms.AddBatchForm
    success_url = reverse_lazy("adminhome")

class Batches(ListView):
    model=Batch
    template_name = "reporting/batch_list.html"
    context_object_name = "batches"

class BatchEdit(UpdateView):
    model=Batch
    template_name = "reporting/batch_edit.html"
    form_class= forms.AddBatchForm
    pk_url_kwarg ="id"
    success_url = reverse_lazy("batches")


class Template(TemplateView):
    template_name= "reporting/base.html"

class SignInView(TemplateView):
    template_name = "reporting/user_login.html"
    form_class=forms.SignInForm
    context={}

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["form"]=self.form_class
        return context

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                if request.user.is_admin:
                    print("success")
                    return redirect("adminhome")
                else:
                    return redirect("userhome")


class UserView(TemplateView):
    template_name = "reporting/user_home.html"

class SignOutView(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")


class AddTimesheetView(CreateView):
    model = Timesheet
    template_name = "reporting/add_timesheet.html"
    form_class = forms.TimesheetForm

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            timesheet=form.save(commit=False)
            timesheet.user=request.user
            timesheet.save()
            return redirect("userhome")

class ListTimesheetView(ListView):
    model = Timesheet
    template_name = "reporting/view_timesheet.html"
    context_object_name = "timesheets"

    def get_queryset(self):
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset

class TimeSheetEdit(UpdateView):
    model=Timesheet
    template_name = "reporting/edit_timesheet.html"
    form_class= forms.TimesheetForm
    pk_url_kwarg ="id"
    success_url = reverse_lazy("userhome")