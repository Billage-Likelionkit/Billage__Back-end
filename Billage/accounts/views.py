from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.routers import DefaultRouter
import json, os
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers

from django.contrib.sites.shortcuts  import get_current_site
from django.utils.http               import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail                import EmailMessage
from django.utils.encoding           import force_bytes, force_str
from django.core.exceptions          import ValidationError
import smtplib
from email.mime.text import MIMEText
from .tokens                import account_activation_token
from .text                  import message


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


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

            user = User.objects.create(email=data['email'], password=data['user_pw'],
                                member_id= User.objects.all().count() + 5432, name=data['name'],
                                phone=data['phone'])
            current_site = get_current_site(request)
            domain = current_site.domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            message_data = message(domain, uidb64, token)

            # 세션 생성
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # TLS 보안 시작
            s.starttls()
            # 로그인 인증
            s.login(get_secret("MAIL_ID"), get_secret("MAIL_PW"))
            # 보낼 메시지 설정
            msg = MIMEText(message(domain, uidb64, token))
            msg['Subject'] = "이메일 인증을 완료해주세요"
            # 메일 보내기
            s.sendmail(get_secret("MAIL_ID"), data['email'], msg.as_string())
            # 세션 종료
            s.quit()
            mail_title = "이메일 인증을 완료해주세요"
            mail_to = data['email']
            email = EmailMessage(mail_title, message_data, to=[mail_to])
            email.send()
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


@method_decorator(csrf_exempt, name='dispatch')
class Activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            if account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return redirect("home.html")

            return JsonResponse({"message": "AUTH FAIL"}, status=400)

        except ValidationError:
            return JsonResponse({"message": "TYPE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEY"}, status=400)


class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer