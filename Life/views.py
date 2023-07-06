from django.shortcuts import render
from django.http import HttpResponse
from Life.models import *
# Create your views here.

def insert_dept(request):
    if request.method=='POST':
        Id=request.POST.get('ids')
        Name=request.POST.get('names')
        Loc=request.POST.get('locs')
        Department.objects.get_or_create(Dept_id=Id,Dept_name=Name,Dept_loc=Loc)[0].save()
        return HttpResponse('<center><h1>Dept added successfully..!!</h1></center>')
    return render(request,'insert_dept.html')

def insert_emp(request):
    LDO=Department.objects.all()
    d={'LDO':LDO}
    if request.method=='POST':
        Eid=request.POST.get('nos')
        Ename=request.POST.get('names')
        Jobu=request.POST.get('jobs')
        Manage=request.POST.get('manages')
        Hire=request.POST.get('hires')
        Sal=request.POST.get('sals')
        Dept=request.POST.get('depts')
        DO=Department.objects.get(Dept_id=Dept)
        Employee.objects.get_or_create(Emp_id=Eid,Emp_name=Ename,Job=Jobu,Manager=Manage,Hire_date=Hire,Salary=Sal,Dept_id=DO)[0].save()
        return HttpResponse('<center><h1>Employee added successfully</h1></center>')
    return render(request,'insert_emp.html',d)