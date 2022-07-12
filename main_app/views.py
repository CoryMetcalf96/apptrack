from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Application, Status
from .forms import ContactForm, StatusForm

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

# APPLICATION DETAIL VIEW (INDIVIDUAL)
def applications_detail(request, application_id):
    application = Application.objects.get(id=application_id)
    status = Status.objects.get(id=application_id)
    # Instantiate the contact form and status form
    contact_form = ContactForm()
    status_form = StatusForm()
    return render(request, 'applications/detail.html', {'application' : application, 'contact_form': contact_form, 'status': status, 'status_form': status_form})

# APPLICATION CREATE CLASS-BASED-VIEW
class ApplicationsCreate(CreateView):
    model = Application
    fields = '__all__'

# APPLICATION UPDATE CLASS-BASED-VIEW
class ApplicationsUpdate(UpdateView):
    model = Application
    fields = '__all__'

# APPLICATION DELETE CLASS-BASED-VIEW
class ApplicationsDelete(DeleteView):
    model = Application
    success_url = '/applications/'

# APPLICATION ADD CONTACT FUNCTION
def add_contact(request, application_id):
    form = ContactForm(request.POST)
    if form.is_valid():
        new_contact = form.save(commit=False)
        new_contact.application_id = application_id
        new_contact.save()
    return redirect('applications_detail', application_id=application_id)

# APPLICATION ADD STATUS FUNCTION
def add_status(request, application_id):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.application_id = application_id
        new_status.save()
    return redirect('applications_detail', application_id=application_id)