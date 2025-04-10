from django.contrib import admin
from .models import Contact, ContactInteraction, JobApplication, UpdateCycle

admin.site.register(Contact)
admin.site.register(ContactInteraction)
admin.site.register(JobApplication)
admin.site.register(UpdateCycle)

