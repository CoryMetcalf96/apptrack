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
    # PATH TO VIEW PRIORITY APPLICATIONS
    path('applications_priority/', views.applications_index_priority, name='applications_index_priority'),
    # PATH TO VIEW PRIORITY APPLICATIONS
    path('applications_follows/', views.applications_index_follows, name='applications_index_follows'),
    # PATH TO VIEW INTERVIEW APPLICATIONS
    path('applications_interviews/', views.applications_index_interviews, name='applications_index_interviews'),
    # PATH TO VIEW OFFER APPLICATIONS
    path('applications_offers/', views.applications_index_offers, name='applications_index_offers'),
    # PATH TO VIEW CLOSED APPLICATIONS
    path('applications_closed/', views.applications_index_closed, name='applications_index_closed'),
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