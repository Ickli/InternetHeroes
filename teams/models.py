from django.db import models
from django.contrib.auth.models import User, Group

TITLE_MAX_LENGTH = 50
ABOUT_MAX_LENGTH = 150
VK_IDENT_MAX_LENGTH = 50
TELEGRAM_IDENT_MAX_LENGTH = 50

NEEDED_GROUPS_THROUGH_NAME = "groups"

class Team(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=False)
    title = models.CharField(max_length = TITLE_MAX_LENGTH)
    about = models.CharField(max_length = ABOUT_MAX_LENGTH)
    isFind = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name = NEEDED_GROUPS_THROUGH_NAME)
    participants = models.ManyToManyField(User, related_name='participants')
    # created_at = models.DateTimeField(auto_now_add=True)
    vk = models.CharField(max_length = VK_IDENT_MAX_LENGTH)
    telegram = models.CharField(max_length = TELEGRAM_IDENT_MAX_LENGTH)

    def __str__():
        return title

