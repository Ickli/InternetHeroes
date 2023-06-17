from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import AdditionalInfo, Like, Image

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'

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
    group_names = serializers.SerializerMethodField()

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

    def get_group_names(self, obj):
        groups = obj.groups.all()
        response = [group.name for group in groups]
        return response

    def get_additional_info(self, obj):
        pass

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
