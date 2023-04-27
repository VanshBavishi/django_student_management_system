from django.shortcuts import render, HttpResponse
from .models import Student, Section, Department
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_students(request):
    emps = Student.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_student.html', context)


def add_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        year = int(request.POST['year'])
        section = int(request.POST['section'])
        CGPA = int(request.POST['CGPA'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        date_of_birth = request.POST['date_of_birth']
        date_of_admission = request.POST['date_of_admission']
        year_of_graduation = int(request.POST['year_of_graduation'])
        
       
        new_student = Student(first_name= first_name, last_name=last_name,year=year, section_id=section, CGPA=CGPA, phone=phone, dept_id = dept, date_of_admission = date_of_admission , date_of_birth = date_of_birth, year_of_graduation = year_of_graduation )
        new_student.save()
        return HttpResponse('Student added Successfully')
    elif request.method=='GET':
        return render(request, 'add_student.html')
    else:
        return HttpResponse("An Exception Occured! Student Has Not Been Added")


def remove_student(request, student_id = 0):
    if student_id:
        try:
            student_to_be_removed = Student.objects.get(id=student_id)
            student_to_be_removed.delete()
            return HttpResponse("Student Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Student.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_Student.html',context)


def filter_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        section = request.POST['section']
        emps = Student.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if section:
            emps = emps.filter(section__name__icontains = section)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_student.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_student.html')
    else:
        return HttpResponse('An Exception Occurred')