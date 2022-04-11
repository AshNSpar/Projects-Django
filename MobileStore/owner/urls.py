from django.urls import path
from owner import views

urlpatterns=[
    path('addmobile',views.add_mobile,name="addphone")
]