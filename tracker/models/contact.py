from django.db import models
from tracker.models import UpdateCycle

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    role = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)