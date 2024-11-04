from django.urls import path

from . import views
app_name = 'studentapp'
urlpatterns = [
 path('StudentHomePage/',views.StudentHomePage,name='StudentHomePage'),
 path('ViewMarks/',views.view_marks,name='ViewMarks'),
]