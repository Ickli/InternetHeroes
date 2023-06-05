from django.db import models
from django.contrib.auth.models import User

TITLE_MAX_LENGTH = 100
SHORT_DESCRIPTION_MAX_LENGTH = 150
FULL_DESCRIPTION_MAX_LENGTH = 500

class RawTask(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    completed = models.BooleanField()
    short_description = models.CharField(max_length=SHORT_DESCRIPTION_MAX_LENGTH)
    full_description = models.TextField(max_length=FULL_DESCRIPTION_MAX_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)
