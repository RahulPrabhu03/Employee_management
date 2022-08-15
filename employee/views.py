from django.shortcuts import render,HttpResponse
from .models import Dependent, Employee,Role,Department
from datetime import datetime
from django.db.models import Q
from django.contrib.auth import login,logout,authenticate

# Create your views here.


def index1(request):
    return render(request,'index1.html')

def admin_login(request):
    error=""
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if user.is_staff:
            
            error="no"
        else:
            error="yes"
            return HttpResponse('Please Enter a Valid EMP id')
            
    return render(request,'admin_login.html',locals())

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    error="no"
    if request.method=='POST':
        first_name=request.POST['first_name'] 
        last_name=request.POST['last_name'] 
        salary=int(request.POST['salary']) 
        bonus=int(request.POST['bonus']) 
        phone=int(request.POST['phone'] )
        dept=int(request.POST['dept'] )
        role=int(request.POST['role'])
        new_user=Employee(first_name=first_name,last_name=last_name,salary=salary, bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_user.save()
        error="no"
        return render(request,'add_emp.html',locals())
    elif request.method=='GET':
        error="yes"
        return render(request,'add_emp.html',locals())
    # else:
    #     return HttpResponse('An Exception Occured !!! Employee Has Not Been Added')


def update_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        
        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method=='GET':
        return render(request,'update_emp.html')
    else:
        
        return HttpResponse('An Exception Occured !!! ')



def remove_emp(request, emp_id=0):
    error="no"
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            error="no"
            return render(request,'remove_emp.html',locals())
        except:
            error="yes"
            return render(request,'remove_emp.html',locals())
    emps=Employee.objects.all()
    context={
        'emps' :emps
    }
    return render(request,'remove_emp.html',context)


def all_dept(request):
    dep=Department.objects.all()
    context={
        'deps':dep
    }
    print(context)
    return render(request,'all_dept.html',context)

def add_dept(request):
    if request.method=='POST':
        name=request.POST['name'] 
        location=request.POST['location'] 
        new_user=Department(name=name,location=location)
        new_user.save()
        return HttpResponse('Department added Successfully') 
    elif request.method=='GET':
        return render(request,'add_dept.html')
    else:
        return HttpResponse('An Exception Occured !!! Department Has Not Been Added')


def logout(request):
    
    return render(request ,'admin_login.html')


def all_dependent(request):
    emps=Dependent.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_dependent.html',context)

def modify_emp(request):
    error=""
    if request.method=="POST":
        e=(request.POST['employee_id'])
        
        emps=Employee.objects.all()
       
        emps=emps.filter(Q(id__icontains=e))
        context={
            'emps':emps
        }
        if emps:
                error="no"
                return render(request,'modify_emp.html',context)
        else:
                error="yes"
    return render(request,'modify_emp.html',locals())
    
        
def modify(request):
    error= ""
    
    employee=Employee.objects.all()
    
   
    if request.method=="POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        dept=request.POST['dept']
        sal=request.POST['salary']
        bo=request.POST['bonus']
        ct=request.POST['contact']
        ro=request.POST['role']
       
        
        employee.first_name=fn
        employee.last_name=ln
        employee.dept.name=dept
        employee.salary=sal
        employee.bonus=bo
        employee.contact=ct
        employee.role.name=ro

        try:
            employee.save()
            error ="no"
            return render(request,'modify.html')
        except:
            error = "yes"
    return render(request,'modify.html',locals())
    