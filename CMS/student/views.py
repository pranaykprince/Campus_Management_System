from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from CMS_admin.models import Attendence,Student
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/student/profile")
        else:
            messages.error(request,'Invalid')
            return redirect("/student/login")
    else:
        return render(request,'student/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/student/login")

def profile(request):
    return render(request,'student/profile.html')

def attendence(request):
    user_id = request.user.id
    student_object=Student.objects.get(user_id=user_id)
    attendence = Attendence.objects.all().filter(student_id=student_object)
    arguments = {'attendance': attendence}
    return render(request,'student/attendence.html',arguments)