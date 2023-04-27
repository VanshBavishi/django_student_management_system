from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('all_student', views.all_students, name='all_student'),
    path('add_student', views.add_student, name='add_student'),
    path('remove_student', views.remove_student, name='remove_student'),
    path('remove_student/<int:student_id>', views.remove_student, name='remove_student'),
    path('filter_student', views.filter_student, name='filter_student'),
    ]
