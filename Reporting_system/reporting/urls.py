from django.urls import path
from reporting import views

urlpatterns = [
    path("home", views.AdminHome.as_view(), name="adminhome"),
    path("users/add", views.UserAdd.as_view(), name="adduser"),
    path("users", views.Users.as_view(), name="users"),
    path("users/edit/<int:id>", views.UserEdit.as_view(), name="edituser"),

    path("courses/add", views.CourseAdd.as_view(), name="addcourse"),
    path("courses", views.Courses.as_view(), name="courses"),
    path("courses/edit/<int:id>", views.CourseEdit.as_view(), name="editcourse"),

    path("batches", views.Batches.as_view(), name="batches"),
    path("batches/add", views.BatchAdd.as_view(), name="addbatch"),
    path("batches/edit/<int:id>", views.BatchEdit.as_view(), name="editbatch"),

    path("base", views.Template.as_view(), name="base"),

    path("accounts/signin", views.SignInView.as_view(), name="signin"),
    path("users/home", views.UserView.as_view(), name="userhome"),
    path("accounts/signout", views.SignOutView.as_view(), name="signout"),

    path("users/timesheets/add", views.AddTimesheetView.as_view(), name="addtimesheet"),
    path("users/timesheets", views.ListTimesheetView.as_view(), name="viewtimesheet"),
    path("users/timesheets/edit/<int:id>", views.TimeSheetEdit.as_view(), name="edittimesheet"),
            ]