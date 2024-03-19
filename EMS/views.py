from django.shortcuts import render
from django.http import HttpResponse
from EMS.models import Employee
#Create your views here.

# class Employee:
#     def _init_(self):
#        self.name=""
#        self.age=0
#        self.address=""
#        self.mobileno=""
#        self.post=""
#        self.salary=0
# def get_N_Employee(n):
#    empList=[]
#    for i in range(1,n+1):
#        emp=Employee()
#        emp.name="ajay"+str(i)
#        emp.age=20+i
#        emp.address="gorkhpuer"+str(i)
#        emp.mobileno="7068009780"+str(i)
#        emp.post="SE"+str(i)
#        emp.salary=4562445.56+i
#        empList.append(emp)
#    return empList    


def view_home(request):
    if request.method=='GET':
        resp=render(request,'EMS/home.html')
        return resp
    elif request.method=='POST':
        empno=int(request.POST.get('txtNo',0))
        # employees=get_N_Employee(empno)
        # d1={'employees':employees}
        # resp=render(request,'EMS/home.html',context=d1)
        # return resp
        # #resp=HttpResponse("<h1>This is My EMS Home Page</h1>")

def view_about(request):
    d1={'a':0}
    resp=render(request,'EMS/about.html',context=d1)
    #resp=HttpResponse("<h1>This is My About Ems Page</h1>")
    return resp

def view_sum(request,a,b):
    resp=HttpResponse("<h1>I am Calling Sum="+str(a+b)+"</h1>")
    return resp



def view_insert_ems(request ):
    if request.method=='GET':
       resp=render(request,'EMS/insertemp.html')
       return resp
    
    elif request.method=='POST':
        if 'btnaddemp' in request.POST:
            emp=Employee()
            emp.name=request.POST.get('txtName','NA')
            emp.age=request.POST.get('txtAge','NA')
            emp.mobileno=request.POST.get('txtMobile','NA')
            emp.address=request.POST.get('txtAddress','NA')
            emp.save()
            resp=HttpResponse("<h1>Epmloyee Inserted SuccessFully!!</h1>")
            return resp
        elif 'btnsearchemp' in request.POST:
            eid=int(request.POST.get('txtEid',0))
            emp=Employee.objects.get(id=eid)
            d1={'emp':emp}
            resp=render(request,'EMS/insertemp.html',context=d1)
            return resp
        elif 'btnupdateemp' in request.POST:
            emp=Employee()
            emp.id=int(request.POST.get('txtEid',0))
            if Employee.objects.filter(id=emp.id).exists():
               emp.name=request.POST.get('txtName','NA')
               emp.age=request.POST.get('txtAge','NA')
               emp.mobileno=request.POST.get('txtMobile','NA')
               emp.address=request.POST.get('txtAddress','NA')
               emp.save()
               resp=HttpResponse("<h1>Epmloyee Updated SuccessFully!!</h1>")
               return resp
        elif 'btndeletemp' in request.POST:
            emp=Employee()
            emp.id=int(request.POST.get('txtEid',0))
            Employee.objects.filter(id=emp.id).delete()
            resp=HttpResponse("<h1>Epmloyee Delete SuccessFully!!</h1>")
            return resp
        elif 'btnshowallemp' in request.POST:
            allemp=Employee.objects.all()
            d1={'employees':allemp}
            resp=render(request,'EMS/insertemp.html',context=d1)
            return resp
        
def findTable(n): #function Defniction
    list_table=[]
    for i in range(1,11):
        t=n*i
        list_table.append(t)
    return list_table


def view_table(request):
        if request.method=='GET':
            resp=render(request,'EMS/table.html')
            return resp
        elif request.method=='POST':
            num=int(request.POST.get('txtNum',0))
            res=findTable(num)
            d1={'ajay':res}
            resp=render(request,'EMS/table.html',context=d1)
            return resp
        