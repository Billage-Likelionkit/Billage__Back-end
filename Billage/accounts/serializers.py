from .models import User
from rest_framework import serializers

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