from django.shortcuts import render       # http://127.0.0.1:8000/lms/home/

# Create your models here.

def view_home(request):
    resp=render(request,'LMS/home.html')
    return resp

def view_register(request):
    resp=render(request,'LMS/register.html')
    return resp

def view_login(request):
    resp=render(request,'LMS/login.html')
    return resp

def view_secure1(request):
    resp=render(request,'LMS/secure1.html')
    return resp

def view_secure2(request):
    resp=render(request,'LMS/secure2.html')
    return resp

def view_unsecure1(request):
    resp=render(request,'LMS/unsecure1.html')
    return resp

def view_unsecure2(request):
    resp=render(request,'LMS/unsecure2.html')
    return resp
