from django.shortcuts import render
from django.http import HttpResponse
from SMS.models import *
from.forms import StudentForm,PaymentDetailsForm
# Create your views here.
def view_home(request):
    return HttpResponse("<h1>This is My Home</h1>")

def view_course_wise_Students(request):
    allcourse=Course.objects.all()
    d1={'courses':allcourse}
    if request.method=='GET':
        c=Course.objects.get(id=1)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'SMS/course.html',context=d1)
        return resp
    elif request.method=='POST':
        cid=int(request.POST.get('txtcid',0))
        c=Course.objects.get(id=cid)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'SMS/course.html',context=d1)
        return resp

def view_student_frm(request):
    if request.method=='GET':
       frm_unbound=StudentForm()
       d1={'form':frm_unbound}
       resp=render(request,'SMS/stufrm.html',context=d1)
       return resp
    elif request.method=='POST':
        frm_unbound=StudentForm(request.POST)
        if frm_unbound.is_valid():  #Server side validtions
           frm_unbound.save()
           resp= HttpResponse("<h1> Student Register Successfully!</h1>")
           return resp
        else:
            frm_unbound=StudentForm()
            resp=render(request,'SMS/stufrm.html',context=d1)
            return resp
            
def view_PaymentDetails_frm(request):
    if request.method=='GET':
       frm_unbound=PaymentDetailsForm
       d1={'form':frm_unbound}
       resp=render(request,'SMS/payfrm.html',context=d1)
       return resp
    elif request.method=='POST':
        frm_unbound=PaymentDetailsForm(request.POST)
        if frm_unbound.is_valid():  #Server side validtions
           frm_unbound.save()
           resp= HttpResponse("<h1> Payment Done Successfully!</h1>")
           return resp
        else:
            frm_unbound=StudentForm()
            resp=render(request,'SMS/payfrm.html',context=d1)
            return resp            

def view_staticFil_Ex(request):
    resp=render(request,'SMS/staticex.html')
    return resp