from django.db import models
from django.contrib.auth.models import User, Group


LOGIN_MAX_LENGTH = 50
ABOUT_MAX_LENGTH = 300
VK_IDENT_MAX_LENGTH = 50
TELEGRAM_IDENT_MAX_LENGTH = 50

# info about:
#   teams
# is in 'teams' app

# info about:
#   roles
# already is in 'User' model


class AdditionalInfo(models.Model):
    user = models.OneToOneField(
            User, 
            on_delete=models.CASCADE, 
            related_name='additional_info',
            blank = True,
            null = True,
            unique = False)
    # image = models.ImageField(upload_to='images/', blank=True, null=False)
    image = models.TextField(blank = True, null = True)
    #course = models.CharField(max_length=50)
    # assume the field has mupltiple contacts divided by '&' char
    #contacts = models.CharField(max_length=150)
    groups = models.ManyToManyField(Group, related_name='info_groups')
    name = models.CharField(max_length = LOGIN_MAX_LENGTH)
    about = models.CharField(max_length = ABOUT_MAX_LENGTH, blank=True, null=True)
    vk = models.CharField(max_length = VK_IDENT_MAX_LENGTH)
    telegram = models.CharField(max_length = TELEGRAM_IDENT_MAX_LENGTH)
    
    def __str__(self):
        return self.name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked', null=True)
    liked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_by', null=True)

class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images', null=False)
    # image = models.ImageField(upload_to='images/', blank=True, null=False)
    image = models.TextField(blank=True, null=True)
