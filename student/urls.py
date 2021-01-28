from django.urls import path
from . import views

app_name = "student"
urlpatterns = [
    path("", views.login_view, name="login"),
    path("index", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("examForm", views.examForm, name="examForm"),
    path("grades", views.grades, name="grades"),
    path("resources", views.resources, name="resources"),
    path("clubs", views.clubs, name="clubs"),
    path("placement", views.placement, name="placement"),
    path("settings", views.settings, name="settings"),
    path("calendar", views.calendar, name="calendar"),
    path("certificate", views.certificate, name="certificate"),
    path("tutionFee", views.tutionFee, name="tutionFee"),
    path("help", views.help, name="help")
]
