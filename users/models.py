from django.db import models
from django.contrib.auth.models import User


# info about:
#   teams
# is in 'teams' app

# info about:
#   roles
# already is in 'User' model

def image_upload_to(instance, filename):
    return 'images/{filename}'.format(filename)


class AdditionalInfo(models.Model):
    user = models.OneToOneField(
            User, 
            on_delete=models.CASCADE, 
            related_name='additional_info')
    course = models.CharField(max_length=50)
    # assume the field has mupltiple contacts divided by '&' char
    contacts = models.CharField(max_length=150)
    
    def __str__(self):
        return self.course

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked', null=True)
    liked = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_by', null=True)

class Image(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images', null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=False)
