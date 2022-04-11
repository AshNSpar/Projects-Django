from django.urls import path
from madmin import views

urlpatterns = [
    path("accounts/signup",views.AddUserView.as_view(),name="signup"),
    path("accounts/login",views.LogInView.as_view(),name="login"),
    path("home",views.MadminHome.as_view(),name="mhome"),
    path("accounts/logout",views.LogOutView.as_view(),name="logout"),
    path("userhome",views.UserHome.as_view(),name="uhome"),

    path("home/add", views.AddDeviceView.as_view(), name="dadd"),

    ]
