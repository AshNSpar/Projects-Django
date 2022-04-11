from django.shortcuts import redirect,render
from django.contrib.auth import authenticate, login, logout
from employer.forms import RegistrationForm, LogInForm, AddCompanyForm, AddJobForm, ApplicationForm
from django.views.generic import CreateView, TemplateView, ListView, UpdateView,DetailView,DeleteView
from employer.models import MyUser,CompanyProfile,ApplicationModel,JobModel,JobseekerProfile
from django.urls import reverse_lazy

# Create your views here.
class AddUserView(CreateView):
    model = MyUser
    form_class = RegistrationForm
    template_name = "employer/signup.html"
    success_url = reverse_lazy("login")

class LogInView(TemplateView):
    form_class = LogInForm
    template_name = "employer/login.html"
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
                if request.user.role == "Applicant":
                    return redirect('jhome')
                else:
                    return redirect("chome")

            else:
                return redirect('jhome')


class LogOutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")

class CompanyHome(TemplateView):
    template_name = "employer/companyhome.html"

class AddCompany(CreateView):
    model= CompanyProfile
    template_name = "employer/add_company.html"
    form_class= AddCompanyForm
    success_url = reverse_lazy("chome")

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(request.user)
    #     return render(request, self.template_name, {"form": form})

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            company=form.save(commit=False)
            company.user=request.user
            company.save()
            return redirect("chome")

        else:
            return render(request,self.template_name,{"form":form})

class ListCompany(ListView):
    template_name = "employer/list_company.html"
    model = CompanyProfile
    context_object_name = "companies"

class UpdateCompany(UpdateView):
    template_name = "employer/edit_company.html"
    model = CompanyProfile
    form_class = AddCompanyForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("clist")


class AddJob(CreateView):
    model= JobModel
    template_name = "employer/add_job.html"
    form_class= AddJobForm
    success_url = reverse_lazy("chome")

class ListJob(ListView):
    template_name = "employer/list_job.html"
    model = JobModel
    context_object_name = "jobs"

class Updatejob(UpdateView):
    template_name = "employer/edit_job.html"
    model = JobModel
    form_class = AddJobForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("jlist")

class ApplicationView(ListView):
    template_name = "employer/list_profiles.html"
    model = ApplicationModel
    context_object_name = "profiles"


class AppliedAppView(CreateView):
    template_name = "employer/list_job.html"
    model = ApplicationModel
    form_class = ApplicationForm

