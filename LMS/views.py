from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorator import is_CheckLoginorRegister

# Create your views here.
def view_home(request):
    resp=render(request,'LMS/home.html')
    return resp
is_CheckLoginorRegister
def view_register(request):
    if request.method=='GET':
        frm_unbound=UserCreationForm()
        d1={'forms':frm_unbound}
        resp=render(request,'LMS/register.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=UserCreationForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=HttpResponse("<h1>User Created SuccessFully!!</h1>")
            return resp
        else:
            d1={'forms':frm_bound}
            resp=render(request,'LMS/register.html',context=d1)
            return resp
        
is_CheckLoginorRegister
def view_login(request):
    if request.method=='GET':
        resp=render(request,'LMS/login.html')
        return resp
    elif request.method=='POST':
        u_name=request.POST.get('txtUserName','NA')
        u_passwd=request.POST.get('txtPassword','NA')
        user=authenticate(request,username=u_name,password=u_passwd) #pawan
        if user is not None:
            login(request,user)
            #resp=HttpResponse("<h1>Login SuccessFully!!</h1>")
            resp=render(request,'LMS/home.html')
            return resp
        else:
            return render(request,'LMS/login.html')
            #return HttpResponse("<h1>Login Failed!!</h1>")

@login_required(login_url='login')
def view_secure1(request):
    resp=render(request,'LMS/secure1.html')
    return resp

@login_required(login_url='login')
def view_secure2(request):
    resp=render(request,'LMS/secure2.html')
    return resp

def view_unsecure1(request):
    resp=render(request,'LMS/unsecure1.html')
    return resp

def view_unsecure2(request):
    resp=render(request,'LMS/unsecure2.html')
    return resp

def view_logout(request):
    logout(request=request)
    return render(request,'LMS/logout.html')