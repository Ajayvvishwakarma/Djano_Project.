from django.db import models

# Create your models here.
class Employee(models.Model):
    #id=models/models.IntegerField() #ID genrate automatacaliy,no need code.
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=20)
    salary=models.DecimalField(max_digits=18,decimal_places=2)
    def __str__(self):
       return self.name
