from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, default='')
    appointment_day = models.CharField(max_length=100, default='')  # Keep for backward compatibility
    appointment_date = models.DateField(null=True, blank=True)  # New date field
    phone = models.CharField(max_length=15, default='')
    email = models.EmailField(default='')
    message = models.TextField(default='')

    def __str__(self):
        return self.name or self.message[:50]