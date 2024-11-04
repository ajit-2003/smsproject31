from django.contrib import admin
from .models import FacultyPost

@admin.register(FacultyPost)
class FacultyPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-pub_date',)
