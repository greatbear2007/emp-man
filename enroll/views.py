from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from.models import Employee
# Create your views here.

def index(request):
    return render(request , 'enroll/index.html')

def view(request):
    emps = Employee.objects.all()
    return render(request , 'enroll/view.html', {'emps': emps} ) 


def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        address = request.POST['address']
        new_emp = Employee(name = name, age = age, salary = salary, bonus = bonus, address = address)
        new_emp.save()
        emps = Employee.objects.all()
        return render(request, 'enroll/view.html', {'emps':emps})
    else:
        return render(request, 'enroll/add.html')



def remove(request):
    emps = Employee.objects.all()
    return render(request , 'enroll/remove.html', {'emps':emps})


def filter(request):
    '''thi=s  is fuilter ing the dayta '''
    if request.method == "POST":
        name = request.POST["name"]
        emps = Employee.objects.all()
        if name:
            print("Asaa")
            emps = emps.filter(name__contains = name)
            return render(request , 'enroll/view.html' , {'emps':emps})
        else:
            return render(request , 'enroll/filter.html')
            
    return render(request , 'enroll/filter.html')

print("Python Class 2PM")