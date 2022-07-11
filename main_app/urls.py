from django.urls import path
from . import views

urlpatterns = [
    # PATH TO GO HOME
    path('', views.home, name='home'),
    # PATH TO GO TO ABOUT PAGE
    path('about/', views.about, name='about'),
    # PATH TO VIEW ALL APPLICATIONS
    path('applications/', views.applications_index, name='applications_index'),
]