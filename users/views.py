from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse
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

    def create(self, request, *args, **kwargs):
        deser = UserRegisterSerializer(data = request.data)
        deser.is_valid(raise_exception = True)
        info = deser.validated_data['additional_info']
        deser.validated_data['additional_info'] = None
        deser_user = User(**deser.validated_data)
        deser_user.save()
        info = AdditionalInfo(**info)
        info.user = deser_user
        info.save()

        return HttpResponse()


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

class UserByLoginView(View):

    def get(self, request, login):
        user = AdditionalInfo.objects.filter(login = login).first().user
        ser_user = UserSerializer(user)
        return JsonResponse(ser_user.data)
