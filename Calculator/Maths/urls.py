from django.urls import path
from Maths import views


urlpatterns=[
    path("addnum",views.add_numbers,name="addnums"),
    path("subnum",views.sub_numbers,name="subnums"),
    path("multnum",views.mult_numbers,name="multnums"),
    path("divnum",views.div_numbers,name="divnums"),
    path("cubenum",views.cube_numbers,name="cubenums"),
    path("",views.index,name="home")

]