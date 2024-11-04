from django.contrib import admin
from .models import Feedback
from django.contrib import admin
from .models import *

admin.site.register(Task)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'feedback')
