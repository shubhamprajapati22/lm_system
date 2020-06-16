from django.contrib import admin
from .models import *

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('libid', 'course', 'user')

admin.site.register(StudentInfo, StudentInfoAdmin)
