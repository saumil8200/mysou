from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def login_view(request):
    # return HttpResponse("<h1>Hello, world</h1>")
    if request.method == "POST":
        # Accessing email and password from form data
        email = request.POST["email"]
        password = request.POST["password"]
        username = User.objects.get(email=email)
        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)
        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("student:index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "student/login.html", {
                "message": "Invalid Credentials"
            })
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("student:index"))
    return render(request, "student/login.html")

def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("student:login"))
    return render(request, "student/index.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("student:login"))

# DashBoard
def dashboard(request):
    if request.method == "GET":
        return render(request, "student/dashboard.html")

# Notification
def notification(request):
    if request.method == "GET":
        return render(request, "student/notification.html")

# Grades
def grades(request):
    if request.method == "GET":
        return render(request, "student/grades.html")

# Resources
def resources(request):
    if request.method == "GET":
        return render(request, "student/resources.html")

# Clubs
def clubs(request):
    if request.method == "GET":
        return render(request, "student/clubs.html")

# Placement
def placement(request):
    if request.method == "GET":
        return render(request, "student/placement.html")

# Profile
def profile(request):
    if request.method == "GET":
        return render(request, "student/profile.html")


# Calendar
def calendar(request):
    if request.method == "GET":
        return render(request, "student/calendar.html")


# Certficate Request
def certificate(request):
    if request.method == "GET":
        return render(request, "student/certificate.html")

# Tution Fees
def tutionFee(request):
    if request.method == "GET":
        return render(request, "student/tutionFee.html")

# Help
def help(request):
    if request.method == "GET":
        return render(request, "student/help.html")

