from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_dept(request):
    dn=input('enter a department name')
    di=input('enter a did ')
    dl=input('enter dlocation')
    DO=Dept.objects.get_or_create(dname=dn,did=di,dlocation=dl)[0]
    DO.save()
    return HttpResponse ('dept is inserted')

def insert_emp(request):
    dn=input('enter a department name')
    DO=Dept.objects.get_or_create(dname=dn)[0]
    DO.save()
    en=input('enter name')
    e=input('enter a number')
    el=input('enter location')
    EO=Emp.objects.get_or_create(dname=DO,ename=en,enumber=e,elocation=el)[0]
    EO.save()
    return HttpResponse ('emp date is inserted')