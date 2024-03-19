from django.urls import path
from .views import *
#Base URL =>> http://127.0.0.1:8000/ems/

urlpatterns=[
path('home/',view_home), 
path('about/',view_about),
path('sum/<int:a>/<int:b>/',view_sum),
path('emphm/',view_insert_ems),
path('tble/',view_table),
]