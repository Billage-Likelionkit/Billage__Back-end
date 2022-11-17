from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta(object):
        model = User
        fields = {'email', 'password'}

    def validate(self, attrs):
        user = authenticate(email=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')
        else:
            token = RefreshToken.for_user(user=user)  # access token 발급을 위해 user의 refresh token을 가져옴
            data = {
                'user' : user.id, 
                'email' : user.email,
                "message": "login successs",
                'refresh_token' : str(token),
                'access_token' : str(token.access_token)
            }   
            return data
        return {'user': user}

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            member_id = validated_data['member_id'],
            name = validated_data['name'],
            phone = validated_data['phone'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['email', 'member_id' , 'name', 'phone' , 'password']