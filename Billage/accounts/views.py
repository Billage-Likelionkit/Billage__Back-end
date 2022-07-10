from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework import views, response, permissions, authentication
from django.contrib.auth import login, logout

class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#로그인
class LoginView(views.APIView):
    # permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return response.Response()


class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_object(self, *args, **kwargs):
        return self.request.user

