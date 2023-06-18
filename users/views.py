from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse
from rest_framework.response import Response
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
        images = deser.validated_data['images']
        gnames = deser.validated_data['group_names']
        deser.validated_data['additional_info'] = None
        del deser.validated_data['images']
        del deser.validated_data['group_names']
        deser_user = User(**deser.validated_data)
        deser_user.save()
        info = AdditionalInfo.objects.get_or_create(**info)[0]
        # print(info)
        info.user = deser_user
        info.save()

        for gname in gnames:
            group = Group.objects.get(name = gname.first().name)
            group.user_set.add(deser_user)

        return Response(UserSerializer(deser_user).data)

    # def update(self, request, *args, **kwargs):
    #     self.create(request, args, kwargs)
    #     # partial = kwargs.pop('partial', False)
    #     # instance = self.get_object()
    #     # serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     # serializer.is_valid(raise_exception=True)
    #     # self.perform_update(serializer)

    #     # # this will return autor's data as a response 
    #     # return Response(AuthorSerializer(instance.parent).data)
    # def partial_update(self, request, *args, **kwargs):
    #     self.create(request, args, kwargs)


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
        user = User.objects.filter(username = login).first()
        # user = AdditionalInfo.objects.filter(login = login).first().user
        ser_user = UserSerializer(user)
        return JsonResponse(ser_user.data)
