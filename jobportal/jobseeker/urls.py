from django.urls import path
from jobseeker import views

urlpatterns=[
    path("profile/add",views.AddProfileView.as_view(),name="padd"),
    path("",views.JobSeekerHome.as_view(),name="jhome"),
    path("profile/list",views.ListProfile.as_view(),name="plist"),
    path("profile/edit/<int:id>",views.EditProfile.as_view(),name="pedit"),

    path("job/list", views.ListJobs.as_view(), name="joblist"),
    path("job/success", views.SuccessApply.as_view(), name="sapply"),

    path("job/jaja", views.Jaja.as_view(), name="japply"),
]