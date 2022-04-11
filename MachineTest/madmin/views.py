from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout
from madmin.forms import RegistrationForm, LogInForm, AddUserForm, AddDeviceForm
from django.views.generic import CreateView, TemplateView, ListView, UpdateView,DetailView,DeleteView
from madmin.models import MyUser,AddUser,AddDevice
from django.urls import reverse_lazy

# Create your views here.
class AddUserView(CreateView):
    model = MyUser
    form_class = RegistrationForm
    template_name = "madmin/signup.html"
    success_url = reverse_lazy("login")

class LogInView(TemplateView):
    form_class = LogInForm
    template_name = "madmin/login.html"
    context = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                if request.user.role == "User":
                    return redirect('uhome')
                else:
                    return redirect("mhome")

            else:
                return redirect('mhome')


class LogOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")

class MadminHome(TemplateView):
    template_name = "madmin/mhome.html"

class UserHome(TemplateView):
    template_name = "madmin/uhome.html"

class AddDeviceView(CreateView):
    model= AddDevice
    template_name = "madmin/adddevice.html"
    form_class= AddDeviceForm
    success_url = reverse_lazy("dadd")

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(request.user)
    #     return render(request, self.template_name, {"form": form})
    #
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST,request.FILES)
    #     if form.is_valid():
    #         company=form.save(commit=False)
    #         company.user=request.user
    #         company.save()
    #         return redirect("chome")
    #
    #     else:
    #         return render(request,self.template_name,{"form":form})
