
from contextlib import nullcontext
from turtle import clear
from urllib import request 
from django.contrib import admin
from django.urls import path
from app import views       

app_name='app'
urlpatterns = [
    
    path('',views.index,name='home'),
    path('Notes_it/index',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'), 
    path('Notes_it/',views.Notes_it,name='Notes_it'),
    path('Notes_cse/',views.Notes_cse,name='Notes_cse'),
    path('Notes_civil/',views.Notes_civil,name='Notes_civil'),
    path('Notes_eee/',views.Notes_eee,name='Notes_eee'),
    path('Notes_ece/',views.Notes_ece,name='Notes_ece'),
    path('Notes_mech/',views.Notes_mech,name='Notes_mech'),
    path('Notes_it/Notes_it_alc',views.Notes_it_alc,name='Notes_it_alc'),
    path('Notes_it/Notes_it_dccn',views.Notes_it_dccn,name='Notes_it_dccn'),
    path('Notes_it/Notes_it_mpi',views.Notes_it_mpi,name='Notes_it_mpi'),
    path('Notes_it/Notes_it_os',views.Notes_it_os,name='Notes_it_os'),
    path('notes_1',views.show_pdf1,name="Notes"),
    path('notes_2',views.show_pdf2,name="Notes"),
    path('notes_3',views.show_pdf3,name="Notes"),
    path('notes_4',views.show_pdf4,name="Notes"),
    path('notes_5',views.show_pdf5,name="Notes"),
    path('notes_6',views.show_pdf6,name="Notes"),


    # path('', views.index, name='index'),
    # path('analysis/', views.show_pdf, name='run')
]