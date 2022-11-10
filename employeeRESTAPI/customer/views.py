from django.shortcuts import render
from django.http import Jsonresponse
# Create your views here.
def get_employee_details(request):
    rollno=1234
    name='priya'
    marks=100
    my_dict={"rollno":rollno,"name"=name,"marks"=marks}
    return Jsonresponse(my_dict)