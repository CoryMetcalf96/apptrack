from django.db import models
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