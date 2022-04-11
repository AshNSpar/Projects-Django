from django.urls import path
from customer import views

urlpatterns=[
    path("accounts/signup",views.signup_view,name="signup")
]