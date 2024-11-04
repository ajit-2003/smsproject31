from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from adminapp.models import StudentList


class FacultyPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'advanced Object-Oriented Programming'),
        ('PFSD', 'Python FUll Stack Development'),
    ]
    SECTION_CHOICES = [
        ('S11', 'SECTION S11'),
        ('S12', 'SECTION S12'),
        ('S13', 'SECTION S13'),
        ('S14', 'SECTION S14'),
        ('S15', 'SECTION S15'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def str(self):
        return f'{self.student.Register_number}-{self.course} ({self.section})'


class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.course}"
