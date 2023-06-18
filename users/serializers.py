from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import AdditionalInfo, Like, Image

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        exclude = ('id',)
        extra_kwargs = {
            'id': {'read_only': False},
            'slug': {'validators': []},
        }

    def to_internal_value(self, data):
        if data['user'] != '':
            info = AdditionalInfo.objects.filter(user=data['user']).first()
            if info is not None:
                info.delete()
        return super().to_internal_value(data)


class GroupNamesField(serializers.Field):
    queryset = Group.objects.all()

    def to_representation(self, obj):
        # print(obj.name)
        # return '[' + ', '.join(group.name for group in obj.groups.all()) + ']'
        return [group.name for group in obj.groups.all()]

    def to_internal_value(self, data):
        return [Group.objects.get(name=gname) for gname in data]

class UserSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
#    additional_info = serializers.PrimaryKeyRelatedField(
#            many=False,
#            queryset=AdditionalInfo.objects.all())
    additional_info = AdditionalInfoSerializer(many=False)
#    liked = serializers.PrimaryKeyRelatedField(
#            many=True,
#            queryset=Like.objects.all(),
#            required=False)
#    liked_by = serializers.PrimaryKeyRelatedField(
#            many=True,
#            queryset=Like.objects.all(),
#            required=False)
    images = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Image.objects.all(),
            required=False)
    group_names = GroupNamesField(source='*', required = False)
    # group_names = GroupNamesField(
    #         many = True,
    #         queryset = Group.objects.all(),
    #         required=False)

    class Meta:
        model = User
        fields = (
                'id',
                'username',
                # 'first_name',
                # 'last_name',
                'group_names',
                # 'email',
                # 'password',
                # 'groups',
                # 'user_permissions',
                # 'is_staff',
                # 'is_active',
                # 'last_login',
                # 'date_joined',
                'additional_info',
                # 'liked',
                # 'liked_by',
                'images'
                )
        extra_kwargs = {
            'id': {'read_only': False},
            'slug': {'validators': []},
        }

    # def create(self, valdata):
    #     images = valdata['images']
    #     valdata['images'] = None
    #     user = User.objects.get_or_create(**valdata)
    #     user.save()

    # def update(self, instance, valdata):
    #     images = valdata['images']
    #     valdata['images'] = None
    #     user = User(**valdata)
    #     user.save()

    # def to_internal_value(self, data):
    #     if data['username'] != '':
    #         user = User.objects.filter(username=data['username']).first()
    #         id = 
    #         if user is not None:
    #             user.delete()
    #     return super().to_internal_value(data)

    def get_group_names(self, obj):
        groups = obj.groups.all()
        response = [group.name for group in groups]
        return response



class UserRegisterSerializer(UserSerializer):
    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + ('password',)
        

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()
    
    class Meta:
        model = Group
        fields = ('name','users')
        lookup_field = 'name'

    def get_users(self, obj):
        users = obj.user_set.all()
        response = [user.id for user in users]
        return response
