from django.shortcuts import render
from django.http import HttpResponse
from .models import Application

# HOME VIEW
def home(request):
    return render(request, 'home.html')

# ABOUT VIEW
def about(request):
    return render(request, 'about.html')

# APPLICATION INDEX VIEW (ALL)
def applications_index(request):
    applications = Application.objects.all()
    return render(request, 'applications/index.html', {'applications': applications})