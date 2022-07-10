from .models import User
from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(email=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

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