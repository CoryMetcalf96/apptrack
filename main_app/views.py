from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application
from .forms import ContactForm, StatusForm

# HOME VIEW
def home(request):
    return render(request, 'home.html')


# ABOUT VIEW
def about(request):
    return render(request, 'about.html')


# SIGNUP VIEW
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('applications_index')
        else:
            error_message = 'Invalid sign up - please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# APPLICATION INDEX VIEW (ALL)
@login_required
def applications_index(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'applications/index.html', {'applications': applications})


# APPLICATION DETAIL VIEW (INDIVIDUAL)
@login_required
def applications_detail(request, application_id):
    application = Application.objects.get(id=application_id)
    status = Application.objects.get(id=application_id)
    # Instantiate the contact form and status form
    contact_form = ContactForm()
    status_form = StatusForm()
    return render(request, 'applications/detail.html', {'application' : application, 'contact_form': contact_form, 'status': status, 'status_form': status_form})


# APPLICATION CREATE CLASS-BASED-VIEW
class ApplicationsCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['company_name', 'date_applied', 'company_website', 'company_summary', 'application_link', 'notes']

    # ASSIGN APPLICATION TO THE LOGGED IN USER
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# APPLICATION UPDATE CLASS-BASED-VIEW
class ApplicationsUpdate(LoginRequiredMixin, UpdateView):
    model = Application
    fields = '__all__'


# APPLICATION DELETE CLASS-BASED-VIEW
class ApplicationsDelete(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = '/applications/'


# APPLICATION ADD CONTACT FUNCTION
@login_required
def add_contact(request, application_id):
    form = ContactForm(request.POST)
    if form.is_valid():
        new_contact = form.save(commit=False)
        new_contact.application_id = application_id
        new_contact.save()
    return redirect('applications_detail', application_id=application_id)


# APPLICATION ADD STATUS FUNCTION
@login_required
def add_status(request, application_id):
    form = StatusForm(request.POST)
    if form.is_valid():
        new_status = form.save(commit=False)
        new_status.application_id = application_id
        new_status.save()
    return redirect('applications_detail', application_id=application_id)