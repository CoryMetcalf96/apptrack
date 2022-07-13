from django.urls import path
from . import views

urlpatterns = [
    # PATH TO GO HOME
    path('', views.home, name='home'),
    # PATH TO GO TO ABOUT PAGE
    path('about/', views.about, name='about'),
    # PATH TO SIGN UP NEW USERS
    path('accounts/signup', views.signup, name='signup'),
    # PATH TO VIEW ALL APPLICATIONS
    path('applications/', views.applications_index, name='applications_index'),
    # PATH TO VIEW INDIVIDUAL APPLICATIONS
    path('applications/<int:application_id>/', views.applications_detail, name='applications_detail'),
    # PATH TO CREATE A NEW APPLICATION
    path('applications/create', views.ApplicationsCreate.as_view(), name='applications_create'),
    # PATH TO UPDATE AN INDIVIDUAL APPLICATION
    path('applications/<int:pk>/update/', views.ApplicationsUpdate.as_view(), name='applications_update'),
    # PATH TO DELETE AN INDIVIDUAL APPLICATION
    path('applications/<int:pk>/delete/', views.ApplicationsDelete.as_view(), name='applications_delete'),
    # PATH TO ADD A CONTACT TO AN INDIVIDUAL APPLICATION
    path('applications/<int:application_id>/add_contact/', views.add_contact, name='add_contact'),
    # PATH TO ADD A STATUS TO AN INDIVIDUAL APPLICATION
    path('applications/<int:application_id>/add_status/', views.add_status, name='add_status'),
]