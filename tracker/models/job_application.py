from django.db import models
from tracker.models import UpdateCycle

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interviewing', 'Interviewing'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
        ('saved', 'Saved'),
    ]
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='saved')
    date_applied = models.DateField(null=True, blank=True)
    job_post_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    update_cycle = models.ForeignKey(UpdateCycle, on_delete=models.CASCADE)