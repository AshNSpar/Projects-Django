from django.urls import path
from patient import views

urlpatterns=[
    path("accounts/signup",views.signup_view,name="signup"),
    path("accounts/signin",views.signin_view,name="signin"),

    path("appointment/booking",views.appoinment_view,name="booking"),
    path("",views.userhome_view,name="userhome"),
]