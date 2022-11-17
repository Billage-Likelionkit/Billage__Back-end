from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path, include
from . import views
from .views import UserListAPI
from rest_framework import urls

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('userlist/', UserListAPI.as_view()),
    path('login/', views.LoginView.as_view()),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',views.LogoutView.as_view()),
 ]