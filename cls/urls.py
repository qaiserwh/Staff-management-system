from os import name
from django.urls import  path
from .import views

urlpatterns = [
     path('', views.admin_login, name='login'),
     path('index',views.index,name='index'),
     path('info',views.info,name='info'),
     path('vacation',views.vac, name='vacation'),
     path('attendance',views.attendance,name='Attendance'),
     path('addatt',views.addatt,name='addatt'),
     path('Trainings',views.tran,name='Trainings'),
     path('addtraning',views.addtraning,name='addtraning'),
     path('addveca',views.addveca,name='addveca'),
     path('admin/',views.Admin,name="admin/"),
  
 ]