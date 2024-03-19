from django.urls import path
from .views import *
#Base URL => http://127.0.0.1:8000/SMS/

urlpatterns = [
    path('home/',view_home),
    path('course/',view_course_wise_Students),
    path('stufrm/',view_student_frm),
    path('payfrm/',view_PaymentDetails_frm),
    path('staticex/',view_staticFil_Ex),
]
