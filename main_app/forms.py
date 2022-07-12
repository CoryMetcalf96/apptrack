from dataclasses import fields
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['date', 'contact_method', 'notes']