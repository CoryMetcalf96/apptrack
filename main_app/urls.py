from django.urls import path
from . import views

urlpatterns = [
    # PATH TO GO HOME
    path('', views.home, name='home'),
    # PATH TO GO TO ABOUT PAGE
    path('about/', views.about, name='about'),
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
]