from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    title = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name='participants')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__():
        return title

