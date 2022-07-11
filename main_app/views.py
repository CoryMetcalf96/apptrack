from django.shortcuts import render
from django.http import HttpResponse

# HOME VIEW
def home(request):
    return render(request, 'home.html')

# ABOUT VIEW
def about(request):
    return render(request, 'about.html')

class Applications:
    def __init__(self, company_name, date_applied, company_website, company_summary, application_link,notes):
        self.company_name = company_name
        self.date_applied = date_applied
        self.company_website = company_website
        self.company_summary = company_summary
        self.application_link = application_link
        self.notes = notes

applications = [
    Applications('Test company', 'Test date', 'https://www.testcompanywebsite.com', 'Test company summary...', 'https://www.testapplicationlink.com', 'Test notes...'),
    Applications('Test company 2', 'Test date', 'https://www.testcompanywebsite.com', 'Test company summary...', 'https://www.testapplicationlink.com', 'Test notes...'),
    Applications('Test company 3', 'Test date', 'https://www.testcompanywebsite.com', 'Test company summary...', 'https://www.testapplicationlink.com', 'Test notes...'),
]


# APPLICATION INDEX VIEW (ALL)
def applications_index(request):
    return render(request, 'applications/index.html', {'applications': applications})