from django.contrib import admin
from .models import Application, Contact, Status

# ADMIN REGISTRATIONS
admin.site.register(Application)
admin.site.register(Contact)
admin.site.register(Status)