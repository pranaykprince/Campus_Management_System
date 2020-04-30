from django.urls import path
from .import views
urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('profile', views.profile),
    path('studentslist', views.studentslist),
    path('addstudent', views.addstudent),
    path('studentslist/<id>/studentattendencelist/', views.studentattendencelist),
    path('studentslist/<id>/studentattendencelist/update', views.update),
    path('studentslist/<id>/studentattendencelist/updateattendance', views.studentattendencelist),
]
