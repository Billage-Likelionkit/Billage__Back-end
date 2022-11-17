from django.shortcuts import render
from .serializers import UserSerializer, LoginSerializer
from .models import User
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework import views, response, permissions, authentication
from django.contrib.auth import login, logout

from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access_token", access_token, httponly=True)
            res.set_cookie("refresh_token", refresh_token, httponly=True)
            
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        token = serializer.validated_data
        #user = serializer.validated_data['user']
        #login(request, user) 레거시
        return Response({"token":token}, status=status.HTTP_200_OK)


class LogoutView(views.APIView):
    def post(self, request):
        #logout(request) 레거시 코드

        response = Response({"message": "Logout success"}, status=status.HTTP_202_ACCEPTED)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response

class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_object(self, *args, **kwargs):
        return self.request.user

