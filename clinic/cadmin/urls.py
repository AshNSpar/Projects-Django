from django.urls import path
from cadmin import views

urlpatterns=[
    path("doctor/add/",views.DoctorCreate_view,name="doctoradd"),
    path("doctor",views.DoctorList_view,name="doctorlist"),
    path("doctor/details/<int:id>",views.DoctorDetails_view,name="doctordetails"),
    path("doctor/remove/<int:id>",views.DoctorRemove_view,name="doctorremove"),
    path("doctor/change/<int:id>",views.DoctorChange_view,name="doctorchange"),
]
