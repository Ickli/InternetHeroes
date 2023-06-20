from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class TeamSerializer(serializers.ModelSerializer):
    queryset = Team.objects.all()

    class Meta:
        model = Team
        fields = '__all__'

class TeamImageSerializer(serializers.ModelSerializer): 
    queryset = TeamImage.objects.all() 

    class Meta:
        model = TeamImage 
        fields = '__all__' 