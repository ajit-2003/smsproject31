from django.contrib import auth
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import FacultyPost
from .forms import FacultyPostForm, MarksForm
from .models import AddCourse
from adminapp.models import StudentList
from .forms import AddCourseForm

def projecthomepage(request):
    return render(request, 'adminapp/ProjectHomePage.html')
def faculty_home(request):
    if request.method == 'POST':
        form = FacultyPostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the blog post to the database
            return redirect('facultyapp:faculty_home')  # Use app_name here to avoid issues
    else:
        form = FacultyPostForm()

    posts = FacultyPost.objects.all()  # Get all blog posts to display them
    return render(request, 'facultyapp/BlogPost.html', {'form': form, 'posts': posts})

def delete_post(request, post_id):
    try:
        post = FacultyPost.objects.get(pk=post_id)
        post.delete()
    except FacultyPost.DoesNotExist:
        pass
    return redirect('facultyapp:faculty_home')

def FacultyHomePage(request):
    return render(request, 'facultyapp/FacultyHomePage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')


def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/add_course.html', {'form': form})


def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/view_student_list.html', context)


def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.user
            user_email = student_user.email

            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = 'majitpatra31@gmail.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'facultyapp/post_marks.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})