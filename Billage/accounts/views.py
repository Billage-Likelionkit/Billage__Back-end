from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.generics import ListAPIView


# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer