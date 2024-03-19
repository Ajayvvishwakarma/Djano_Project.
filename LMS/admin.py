from django.contrib import admin
from SMS.models import Student
# Register your models here.

#admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','mobileno','created_date']