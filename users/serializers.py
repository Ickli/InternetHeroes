from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import AdditionalInfo, Like, Image

class UserSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
    additional_info = serializers.PrimaryKeyRelatedField(
            many=False,
            queryset=AdditionalInfo.objects.all())
    liked = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Like.objects.all(),
            required=False)
    liked_by = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Like.objects.all(),
            required=False)
    images = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Image.objects.all(),
            required=False)

    class Meta:
        model = User
        fields = (
                'id',
                'username',
                'first_name',
                'last_name',
                # 'email',
                # 'password',
                'groups',
                # 'user_permissions',
                # 'is_staff',
                # 'is_active',
                # 'last_login',
                # 'date_joined',
                'additional_info',
                'liked',
                'liked_by',
                'images'
                )

class UserRegisterSerializer(UserSerializer):
    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + ('email', 'password')

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalInfo
        fields = '__all__'

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
