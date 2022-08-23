from unicodedata import name
from . import views
from django.urls import path
urlpatterns = [
    path('',views.Home,name="home"),
    path('about-us/',views.About_us,name='about-us'),
    path('services/',views.Services,name='services'),
    path('single_service/',views.Single_Service,name='single_service'),
    path('Appointment/',views.Appointment,name='Appointment'),

    path('team/',views.Teams,name='team'),
    path('contect-us/',views.Contect_us,name='contect-us'),

]
