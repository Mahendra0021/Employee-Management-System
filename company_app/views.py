from django.shortcuts import render
from .models import Department,Role,Employee
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Q

def Home(request):
    return render(request, 'home.html')

def All_Employee(request):
    emps=Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)  
    return render(request,'All_Employee.html',context)


def Add_Employee(request):
    if request.method == "POST":
        First_name = request.POST['fname']
        Last_name = request.POST['lname']
        salary = request.POST['salary']
        dpartment = request.POST['Department']
        role=request.POST['role']
        bonus = request.POST['bonus'] 
        phone = request.POST['phone']
        add_Emp= Employee(
            First_name=First_name,
            Last_name=Last_name,
            dpartment_id=dpartment,
            salary=salary,
            bonus=bonus,
            role_id=role,
            phone=phone,
            # date=datetime.new()
            )
        add_Emp.save()
        return HttpResponse("<h1>Employee Added Successfully</h1>")
    elif request.method == "GET":
        return render(request,'Add_Employee.html')

def Remove_Employee(request,id=0):
    if id:
        try:
            emp_remove=Employee.objects.get(id=id)
            emp_remove.delete()
            return HttpResponse("<h1><b> Employee removed Successfully <a href='http://127.0.0.1:8000/Remove-Employee'><b>BACK</a></h1>")
        except:
            return HttpResponse("Please Enter A Valid EMP ID<a href='http://127.0.0.1:8000/Remove-Employee'><b>BACK</a>")
        
    emp=Employee.objects.all()
    for i in emp:
        return render(request,'Remove_Employee.html',{'emp':emp})

def Filter_Employee(request):
    print("mahendra")
    if request.method == "POST":
        name = request.POST['fname']
        dpartment = request.POST['Department']
        role = request.POST['role']
        emp = Employee.objects.all()
        if name:
            emp = emp.filter(Q(First_name__icontains = name) | Q(Last_name__icontains = name))

        if dpartment:
            emp=emp.filter(dpartment__name = dpartment)
        if role:
            emp=emp.filter(role__name = role)
        context = {
            'emp':emp
        }
        return render(request, 'All_Employee.html',context)
    elif request.method == "GET":
        return render(request,'Filter_Employee.html')
    else:
        return HttpResponse("An Exception Dccurred")