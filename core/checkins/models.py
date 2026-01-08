from django.db import models
from django.contrib.auth.models import User

class CheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accomplishments = models.TextField()
    blockers = models.TextField(blank=True)
    next_priorities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Check-in by {self.user.username} on {self.created_at.date()}"
