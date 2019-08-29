from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Instructor, Student, Attendance, Guardian
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from functools import reduce

from datetime import datetime
from django.db.models import Sum

from .form import *

# Index Page
def index(request):
    instructor = Instructor.objects.get(id=1)
    return render(request, 'student/index.html', context={'instructor': instructor})

# Instructor Page
class InstructorIndexView(generic.ListView):
    template_name = 'student/instructor.html'

    def get_queryset(self):
        return Instructor.objects.all()
        
# Student Index Page
class StudentIndexView(generic.ListView):
    template_name = 'student/student.html'

    def get_queryset(self):
        return Student.objects.all()

# Student Detail Page
def studentdetail(request, pk):
    student_detail = Student.objects.get(pk=pk)
    guardian_detail = student_detail.guardian
    attendance_detail = Attendance.objects.filter(student=pk)

    context = {
        'stu': student_detail,
        'guardian': guardian_detail,
        'attendance': attendance_detail,
            }
    return render(request, 'student/detail.html', context)


def student_create(request):
    if request.POST:
        stu_form = StudentForm(request.POST or None, prefix="student")
        guardian_form = GuardianForm(request.POST or None, prefix="guardian")
        if stu_form.is_valid() and guardian_form.is_valid():
            if guardian_form.has_changed():
                guardian = guardian_form.save()
                student = stu_form.save(commit=False)
                student.guardian = guardian
            student = stu_form.save(commit=False)
            stu_form.save()
            stu = Student.objects.all()
            return render(request, 'student/student.html', {'object_list': stu})
    else:
        stu_form = StudentForm(request.POST or None, prefix="student")
  
        guardian_form = GuardianForm(request.POST or None, prefix="guardian")
        return render(request, 'student/student_form.html', {"form": stu_form, "form2": guardian_form})

class StudentUpdate(UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'street_name', 'city', 'province', 'postal_code', 'date_of_birth', 'date_of_joining', 'phone_number', 'rank',]

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student:student')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def student_search(request):
    template = 'student/student.html'

    query = request.GET.get('q')

    results = Student.objects.filter(Q(pk__icontains=query) |
                                     Q(first_name__icontains=query) |
                                     Q(last_name__icontains=query) |
                                     Q(guardian__first_name__icontains=query) |
                                     Q(guardian__last_name__icontains=query))

    context = {
        'object_list': results
    }

    return render(request, template, context)



def guardian_create(request, pk):
    if request.POST:
        guardian_form = GuardianForm(request.POST or None, prefix="guardian")
        student = Student.objects.get(pk=pk)
        if guardian_form.is_valid():
            guardian = guardian_form.save()
            student.guardian = guardian
            student.save(force_update=True)
            stu = Student.objects.get(pk=pk)
            return render(request, 'student/student.html', {"object_list": stu})
    else:
        guardian_form = GuardianForm(request.POST or None, prefix="guardian")
        return render(request, 'student/student_form.html', {"form": guardian_form})




class GuardianCreate(CreateView):
    model = Guardian
    fields = ['first_name', 'last_name', 'street_name', 'city', 'province', 'postal_code', 'phone_number']



# Attendance Page
class AttendanceIndexView(generic.ListView):
    template_name = 'student/attend.html'

    def get_queryset(self):
        return Attendance.objects.all()

class AttendanceCreate(CreateView):
    model = Attendance
    fields = ['student', 'attendance_date', 'attendance_count']

class AttendanceUpdate(UpdateView):
    model = Attendance
    fields = ['student', 'attendance_date', 'attendance_count']

class AttendanceDelete(DeleteView):
    model = Attendance
    success_url = reverse_lazy('student:attend')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def attendance_search(request):
    template = 'student/attend.html'

    query = request.GET.get('q')

    results = Attendance.objects.filter(Q(attendance_date__icontains=query) |
                                        Q(student__first_name__icontains=query) |
                                        Q(student__last_name__icontains=query))

    context = {
        'object_list': results
    }

    return render(request, template, context)



