from dataclasses import fields
from django.forms import ModelForm
from .models import Contact, Status

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['date', 'contact_method', 'notes']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['application_status', 'is_priority']