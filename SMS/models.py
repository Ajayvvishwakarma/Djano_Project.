from django.db import models

# Create your models her.
class Student(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False) #Mandatory fild
    age=models.IntegerField()
    mobileno=models.CharField(max_length=20)
    dob=models.DateField(null=True,blank=True)
    pic=models.ImageField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_modified_date=models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.name
    
class Course(models.Model):
    name=models.CharField(max_length=100)
    students=models.ManyToManyField(Student,null=True,blank=True)
    def __str__(self):
        return self.name
    
class PaymentDetails(models.Model):
    amount=models.IntegerField()
    payment_mode=models.CharField(max_length=100,choices=[('Cash','Cash'),('Debit Card','Debit Card'),('Credit Card','Credit Card'),('PayTM','PayTM')])
    payment_date=models.DateTimeField(auto_now=True)
    student=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)

    