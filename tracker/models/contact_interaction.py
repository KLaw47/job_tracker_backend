from django.db import models
from tracker.models import Contact, JobApplication, UpdateCycle

class ContactInteraction(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='interactions')
    job_application = models. ForeignKey(JobApplication, on_delete=models.SET_NULL, null=True, blank=True, related_name='contact_interactions')
    update_cycle = models.ForeignKey(UpdateCycle, on_delete=models.CASCADE, related_name='contact_interactions')
    date = models.DateField()
    type = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.contact.name} - {self.type} on {self.date}"