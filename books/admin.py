from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'author', 'no_of_copies')
admin.site.register(Books, BookAdmin)

class IssueBookAdmin(admin.ModelAdmin):
    list_display = ('code', 'user','returndate', 'is_return')
admin.site.register(IssueBooks, IssueBookAdmin)
