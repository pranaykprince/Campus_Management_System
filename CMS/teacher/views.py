from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from CMS_admin.models import Attendence,Student,Class,Teacher
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    return render(request,'CMS/index.html') 

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/teacher/profile")
        else:
            messages.error(request,'Invalid')
            return redirect("/teacher/login")
    else:
        return render(request,'teacher/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/teacher/login")

def profile(request):
    return render(request,'teacher/profile.html')

def studentslist(request):
    user_id = request.user.id
    teacher_obj = Teacher.objects.get(user_id=user_id)
    Student_obj = Student.objects.filter(class_id=teacher_obj.class_id)
    user_obj = User.objects.all()
    arguments = {'user_id': user_id,'teacher_obj':teacher_obj,'Student_obj':Student_obj,'user_obj':user_obj}
    return render(request,'teacher/students.html',arguments)

def studentattendencelist(request,id):
    student_object=Student.objects.get(id=id)
    attendence = Attendence.objects.all().filter(student_id=student_object)
    arguments = {'attendance': attendence}
    if request.method == 'POST':
        id=request.POST.get('id',)
        h1=request.POST.get('h1',False)
        h2=request.POST.get('h2',False)
        h3=request.POST.get('h3',False)
        h4=request.POST.get('h4',False)
        h5=request.POST.get('h5',False)
        h6=request.POST.get('h6',False)
        print(h1)
        print(h2)
        print(h3)
        print(h4)
        print(h5)
        print(h6)
        Attendence.objects.filter(id=id).update(h1=h1,h2=h2,h3=h3,h4=h4,h5=h5,h6=h6)
        return render(request,'teacher/studentattendencelist.html',arguments)
    return render(request,'teacher/studentattendencelist.html',arguments)

def update(request,id):
    if request.method == 'POST':
        dateid=request.POST['dateid']
        student_object=Student.objects.get(id=id)
        attendence = Attendence.objects.all().filter(id=dateid)
        arguments = {'attendance': attendence}
        return render(request,'teacher/update.html',arguments)

def addstudent(request):
    if request.method == 'POST':
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        class_id=request.POST['class']
        print(email)
        print(fname)
        print(lname)
        print(password)
        print(confirmpassword)
        print(class_id)
        if password == confirmpassword :
            print("same")
            user=User.objects.create_user(first_name=fname,last_name=lname,username=email,email=email,password=password)
            user.save()
            user_select=User.objects.get(username=email)
            class_new=Class.objects.get(class_name=class_id) 
            student_new=Student(user_id=user_select,class_id=class_new)
            student_new.save()
            messages.success(request,'Success')
            return redirect("/teacher/studentslist")
        else:
            messages.error(request,'Invalid')
            return redirect("/teacher/addstudent")
    else:
        userid = request.user.id
        print(userid)
        teacher_object=Teacher.objects.raw('SELECT * FROM CMS_admin_teacher')
        arguments = {'teacher_object': teacher_object,}
        return render(request,'teacher/addstudent.html',arguments)