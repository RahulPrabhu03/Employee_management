from django.contrib import admin
from django.urls import path,include
from employee.views import *

urlpatterns = [
    path('',index1,name="index1"),
    path('home',home,name="home"),
    path('about',about,name="about"),
    path('admin_login',admin_login,name="admin_login"),
    path('index',index,name='index'),
    path('all_emp',all_emp,name='all_emp'),
    path('add_emp',add_emp,name='add_emp'),
    path('remove_emp',remove_emp,name='remove_emp'),
    path('update_emp',update_emp,name='update_emp'),
    path('modify_emp',modify_emp,name='modify_emp'),
    path('modify',modify,name='modify'),
    path('remove_emp/<int:emp_id>',remove_emp,name='remove_emp'),
    path('all_dept',all_dept,name='all_dept'),
    path('add_dept',add_dept,name='add_dept'),
    path('home',add_dept,name='add_dept'),
    path('logout',admin_login,name='logout'),
    path('all_dependent',all_dependent,name='dependent'),






]
