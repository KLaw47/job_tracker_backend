from django.db import models

class UpdateCycle(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.start_date} – {self.end_date})"