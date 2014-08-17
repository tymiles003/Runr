from django.db import models
from django.utils import timezone

class Timer(models.Model):
    key = models.SlugField(primary_key=True)
    text = models.CharField(max_length=100, blank=True)
    creator = models.CharField(max_length=20, blank=True)
    end_time = models.DateTimeField()
    
    def expired(self):
        return self.end_time < timezone.now()
    expired.boolean = True
    expired.short_description = 'Expired?'
