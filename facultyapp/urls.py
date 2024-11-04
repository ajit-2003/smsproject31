from django.urls import path
from . import views

app_name = 'facultyapp'

urlpatterns = [
    path('', views.faculty_home, name='faculty_home'),
    path('', views.projecthomepage, name='projecthomepage'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('FacultyHomePage/', views.FacultyHomePage, name='FacultyHomePage'),
    path('logout/', views.logout, name='logout'),
    path('add_course/', views.add_course, name='add_course'),
    path('view_student_list/', views.view_student_list, name='view_student_list'),
    path('post_marks/', views.post_marks, name='post_marks'),
]
