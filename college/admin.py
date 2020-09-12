from django.contrib import admin
from college.models import Notice,Student
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class NoticeAdmin(ModelAdmin):
    list_display = ['subject','cr_date']
    search_fields = ['subject','msg']
    list_filter = ['cr_date']

admin.site.register(Notice,NoticeAdmin)

class StudentAdmin(ModelAdmin):
    list_display = ['name']
    search_fields = ['name','address']
    list_filter = ['address']

admin.site.register(Student,StudentAdmin)