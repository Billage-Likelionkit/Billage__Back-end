from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.routers import DefaultRouter
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers


# 회원가입
@csrf_exempt
def logout(request):
    if request.session.get('user'):
        del (request.session['user'])
    return redirect('home:home')


@csrf_exempt
def search(request):
    data = json.loads(request.body)
    user = User.objects.filter(member_id=data['member_id'])
    if user:
        context = user.values()[0]
        return JsonResponse(context, status=200, safe=False)
    else:
        context = {"result" : "User가 없습니다"}
        return JsonResponse(context, status=400, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CreateView(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        if User.objects.filter(email=data['email']).exists():
            context = {
                "result": "이미 존재하는 email입니다!"
            }
            return JsonResponse(context, status=400)

        else:
            if data['user_pw'] != data['check_pw']:
                context = {
                    "result": "확인 비밀번호가 일치하지 않습니다!"
                }
                return JsonResponse(context, status=400)

            User.objects.create(email=data['email'], password=data['user_pw'],
                                member_id= User.objects.all().count() + 5432, name=data['name'],
                                phone=data['phone'])
            context = {
                "result": "email을 확인해주세요!"
            }
            return render(request, 'home/home.html', context)

    @csrf_exempt
    def get(self, request):
        return render(request, 'home/register.html')


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)

        if User.objects.filter(email = data['email'], password = data['user_pw']).exists():
            user = User.objects.get(email=data['email'])
            request.session['user'] = data['email']
            context = {"login_stat": "login_ok"}
            return render(request, 'home/home.html', context)
        else:
            context = {
                "result": "id 또는 pw가 틀렸습니다"
            }
            return JsonResponse(context, status=400)

    @csrf_exempt
    def get(self, request):
        return render(request, 'home/login.html')


class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer