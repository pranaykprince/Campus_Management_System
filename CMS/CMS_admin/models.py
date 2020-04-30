from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
      department_name = models.CharField(max_length=25,unique=True)
      def __str__(self):
        return self.department_name

class Class(models.Model):
      department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
      class_name = models.CharField(max_length=25,unique=True)
      def __str__(self):
        return self.class_name

#class UserProfileStatus(models.Model):
#      user_id = models.OneToOneField(User,on_delete=models.CASCADE)
#      user_status_options = (
#            ('S','Student'),
#            ('T','Teacher'),
#          )
#      user_status = models.CharField(max_length=1, choices=user_status_options)
#      class_id = models.ForeignKey(Class,on_delete=models.CASCADE) 
#      def __str__(self):
#        return self.user_id.username

class Teacher(models.Model):
      user_id = models.OneToOneField(User,on_delete=models.CASCADE)
      class_id = models.ForeignKey(Class,on_delete=models.CASCADE) 
      def __str__(self):
        return self.user_id.username

class Student(models.Model):
      user_id = models.OneToOneField(User,on_delete=models.CASCADE)
      class_id = models.ForeignKey(Class,on_delete=models.CASCADE) 
      def __str__(self):
        return self.user_id.username

class Attendence(models.Model):
     ATTENDENCE_STATUS = (
        ('A', 'Absent'),
        ('F', 'Full Day'),
        ('H', 'Half Day'),
       )
     teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
     student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
     date = models.DateField(blank=False)
     h1 = models.BooleanField(default=False)
     h2 = models.BooleanField(default=False)
     h3 = models.BooleanField(default=False)
     h4 = models.BooleanField(default=False)
     h5 = models.BooleanField(default=False)
     h6 = models.BooleanField(default=False)
     attendence_status = models.CharField(max_length=1,choices=ATTENDENCE_STATUS,default='A')
     def __str__(self):
        return self.student_id.user_id.username