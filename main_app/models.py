from django.db import models
from django.urls import reverse
from datetime import date


# APPLICATION MODEL
class Application(models.Model):
    company_name = models.CharField(max_length=100)
    date_applied = models.DateField(default=date.today)
    company_website = models.CharField(max_length=200)
    company_summary = models.TextField(max_length=1000)
    application_link = models.CharField(max_length=200)
    notes = models.TextField(max_length=1000)

    # STR METHOD
    def __str__(self):
        return self.company_name

    # REDIRECT BACK TO DETAIL PAGE AFTER APPLICATION CREATION
    def get_absolute_url(self):
        return reverse('applications_detail', kwargs={'application_id': self.id})


# CONTACT MODEL
CONTACT_METHODS = (
    ('P', 'Phone'),
    ('E', 'Email'),
    ('S', 'Social Media'),
    ('I', 'In-person'),
    ('O', 'Other')
)

class Contact(models.Model):
    date = models.DateField()
    contact_method = models.CharField(max_length=1, choices=CONTACT_METHODS, default=CONTACT_METHODS[0][0])
    notes = models.TextField(max_length=250)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    def __str__(self):
        return f'Method of contact: {self.get_contact_method_display()} on {self.date}.'