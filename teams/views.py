from django.shortcuts import render
from django.views import View 
from django.http import JsonResponse 
from rest_framework import viewsets

from .models import Team, TeamImage
from .serializers import *

class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamImageViewset(viewsets.ModelViewSet): 
    queryset = TeamImage.objects.all() 
    serializer_class = TeamImageSerializer 

class TeamImagesView(View): 

    def get(self, request, pk): 
        team = Team.objects.get(id = pk) 
        response = TeamImageSerializer(TeamImage.objects.filter(team = team), many=True) 
        return JsonResponse(response.data, safe = False) 