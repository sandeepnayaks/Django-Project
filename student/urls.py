from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    # Index Page
    path('', views.index, name='index'),

    # Instructor Page
    path('instructor/', views.InstructorIndexView.as_view(), name='instructor'),

    # Student Pages
    path('student/', views.StudentIndexView.as_view(), name='student'),
    #path('student/add', views.StudentCreate.as_view(), name="student-add"),
    path('student/add', views.student_create, name="student-add"),
    path('student/update/<pk>', views.StudentUpdate.as_view(), name="student-update"),
    path('student/delete/<pk>', views.StudentDelete.as_view(), name="student-delete"),
    path('student/<pk>', views.studentdetail, name='detail'),
    path('student/<pk>/guardian', views.GuardianCreate.as_view(), name='student-guardian'),

  

   

    # Attendance Pages
    path('attend/', views.AttendanceIndexView.as_view(), name='attend'),
    path('attend/add', views.AttendanceCreate.as_view(), name='attend-add'),
    path('attend/update/<pk>', views.AttendanceUpdate.as_view(), name='attend-update'),
    path('attend/delete/<pk>', views.AttendanceDelete.as_view(), name='attend-delete'),





    # Search Pages
    path('studentsearch/', views.student_search, name="student-search"),
    
    path('attendancesearch/', views.attendance_search, name="attend-search"),
   
]
