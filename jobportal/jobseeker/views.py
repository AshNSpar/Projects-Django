from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from jobseeker import forms
from django.views.generic import CreateView,UpdateView,TemplateView,DeleteView,ListView
from employer.models import JobseekerProfile,ApplicationModel,JobModel

# Create your views here.
class AddProfileView(CreateView):

    model = JobseekerProfile
    template_name = "jobseeker/addprofile.html"
    # success_url = reverse_lazy("jhome")
    form_class = forms.ProfileForm

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect("padd")

        else:
            return render(request,self.template_name,{"form":form})


class JobSeekerHome(TemplateView):
    template_name = "jobseeker/jobhome.html"

class ListProfile(ListView):
    model = JobseekerProfile
    template_name = "jobseeker/listprofile.html"
    context_object_name = "profiles"

class EditProfile(UpdateView):
    model = JobseekerProfile
    template_name = "jobseeker/editprofile.html"
    form_class = forms.ProfileForm
    success_url = reverse_lazy("plist")
    pk_url_kwarg = "id"

class ListJobs(ListView):
    template_name = "jobseeker/list_job.html"
    model = JobModel
    context_object_name = "jobs"

class SuccessApply(TemplateView):
    template_name = "jobseeker/success.html"

class Jaja(TemplateView):
    template_name = "jobseeker/jaja.html"

