from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import *
from .models import AdditionalInfo, Like, Image


class AdditionalInfoViewset(viewsets.ModelViewSet):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return UserRegisterSerializer
        return UserSerializer

class LikeViewset(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = "name"
    lookup_value_regex = "[^/]+"
