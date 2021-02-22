from django.urls import path
from . import views

app_name = "student"
urlpatterns = [
    path("", views.login_view, name="login"),
    path("app", views.index, name="index"),
    path("logout", views.logout_view, name="logout"),
    path("app/<str:search>", views.templates, name="index"),
    path("admin/<str:search>", views.templates, name="index"),
]
