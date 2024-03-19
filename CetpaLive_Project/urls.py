"""
URL configuration for CetpaLive_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render

def view_sum(request,a,b,c):
    return HttpResponse("<h1>Hello I am Calling Sum...</h1>"+str(a+b))

def view_sub(request):
    resp= HttpResponse("<h1>Hello I am Calling Sub...</h1>")
    return resp

def view_mult(request):
    resp=HttpResponse("<h1>Hello I am calling MULT...</h1>")
    return resp

def view_div(request):
    resp= HttpResponse("<h1>Hello I am Calling div...</h1>")
    return resp

def view_calc(request):
    a=int(request.POST.get('txtFirst',0))
    b=int(request.POST.get('txtSecond',0))
    if request.method=='GET':
        resp=render(request,'calculator.html')
        return resp
    elif request.method=='POST':
        if 'btnsum' in request.POST:
            c=a+b
        elif 'btnsub' in request.POST:
            c=a-b
        elif 'btnmult' in request.POST:
            c=a*b
        elif 'btndiv' in request.POST:
            c=a/b      
        d1={'a':a,'b':b,'c':c}
        resp=render(request,'calculator.html',context=d1)
        return resp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajay/<int:a>/<int:b>/',view_sum),    #https://127.0.0.1:8000/ajay/
    path('sub/',view_sub),    
    path('mult/',view_mult),   
    path('div/',view_div),     
    path('calc/',view_calc),
    path('ems/',include('EMS.urls')),  #htttp://127.0.0.1:8000/ems
    path('SMS/',include('SMS.urls')),  #htttp://127.0.0.1:8000/sms
    path('LMS/',include('LMS.urls')),  #htttp://127.0.0.1:8000/lms
] 
