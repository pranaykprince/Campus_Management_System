from django.contrib import admin
from . models import Department,Class,Teacher,Student,Attendence
# Register your models here.
admin.site.register(Department)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Attendence)