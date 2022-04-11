from django.urls import path
from employer import views

urlpatterns = [
    path("accounts/signup",views.AddUserView.as_view(),name="signup"),
    path("accounts/login",views.LogInView.as_view(),name="login"),
    path("home",views.CompanyHome.as_view(),name="chome"),
    path("accounts/logout",views.LogOutView.as_view(),name="logout"),

    path("home/add",views.AddCompany.as_view(),name="cadd"),
    path("home/list", views.ListCompany.as_view(), name="clist"),
    path("home/edit/<int:id>", views.UpdateCompany.as_view(), name="cedit"),


    path("job/add",views.AddJob.as_view(),name="jadd"),
    path("job/list", views.ListJob.as_view(), name="jlist"),
    path("job/edit/<int:id>", views.Updatejob.as_view(), name="jedit"),

    path("home/profiles", views.ApplicationView.as_view(), name="appview"),



]