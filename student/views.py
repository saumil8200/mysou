from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import AdminData, StudentData

# Create your views here.

def login_view(request):
    if request.method == "GET":
        try:
            if request.session['user']:
                return HttpResponseRedirect(reverse("student:index"))
            else:
                return render(request, "student/login.html")
        except:
            return render(request, "student/login.html")
    
    if request.method == "POST":
        # Accessing email and password from form data
        user = request.POST["username"]
        passwd = request.POST["password"]
        role = request.POST["role"]
        dept = request.POST["dept_id"]
        print(user,passwd,role,dept)

        if role == "admin":
            try:
                AdminData.objects.get(username=user, password=passwd, dept_id=dept, admin=True)
                request.session['user'] = user
                request.session['admin'] = True
                return HttpResponseRedirect(reverse("student:index"))
            except:
                return render(request, "student/login.html", {
                    "message": "Invalid Credentials"
                })
        elif role == "student":
            try:
                StudentData.objects.get(username=user, password=passwd, dept_id=dept)
                request.session['user'] = user
                request.session['admin'] = False
                print("Logged In")
                return HttpResponseRedirect(reverse("student:index"))
            except:
                return render(request, "student/login.html", {
                    "messageAlert": "Invalid Credentials"
                })
    return render(request, "student/login.html")

def index(request):
    if request.method == "GET":
        try:
            if request.session['user']:
                flag = request.session['admin']
                if flag == True:
                    return render(request, "faculty/index.html")
                else:
                    print("Called")
                    return render(request, "student/index.html")
        except:
            print("Exception")
            return HttpResponseRedirect(reverse("student:login"))

def logout_view(request):
    # logout(request)
    try:
        del request.session['user']
        del request.session['admin']
        return HttpResponseRedirect(reverse("student:login"))
    except:
        return HttpResponseRedirect(reverse("student:login"))


def templates(request,search):
    if request.method == "GET":
        try:
            if request.session['user']:
                user = request.session['user']
                flag = request.session['admin']
                print(flag)
                if flag == True:
                    data = AdminData.objects.get(username=user)
                    return render(request, f"faculty/{search}.html",{
                        "data": data
                    })
                else:
                    data = StudentData.objects.get(username=user)
                    return render(request, f"student/{search}.html",{
                        "data": data
                    })
        except:
            return HttpResponseRedirect(reverse("student:login"))
    if request.method == "POST":
        try:
            if request.session['admin'] == True and request.session['user']:
                # print("posting Data")
                user = request.POST["username"]
                passwd = request.POST["password"]
                dept = request.POST["dept_id"]
                role = request.POST["role"]
                print(user,passwd,dept,role)
                if role == "admin":
                    try:
                        form = AdminData(username=user, password=passwd, dept_id=dept,admin=True)
                        form.save()
                        return render(request, "faculty/register.html", {
                                "messageSuccess": "Admin Created"
                            })
                    except:
                        return render(request, "faculty/register.html", {
                            "messageAlert": "User Already Exist"
                            })
                elif role == "student":
                    try:
                        form = StudentData(username=user, password=passwd, dept_id=dept)
                        form.save()
                        return render(request, "faculty/register.html", {
                                "messageSuccess": "User Created"
                            })
                    except:
                        return render(request, "faculty/register.html", {
                                "messageAlert": "User Already Exist"
                            })
        except:
            return render(request, "faculty/register.html", {
                                "messageAlert": "Error While Creating User"
                            })
