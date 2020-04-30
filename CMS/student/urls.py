from django.urls import path
from .import views
urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('profile', views.profile),
    path('attendence', views.attendence),
]
