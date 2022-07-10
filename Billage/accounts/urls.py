from django.urls import path, include
from . import views
from .views import UserListAPI, LoginView, CreateView, logout, search, Activate
from rest_framework import urls


urlpatterns =[
    path('', search),
    path('signup/', CreateView.as_view()),
    path('signout/', logout),
    path('signin/', LoginView.as_view()),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view()),

    path('api-auth/', include('rest_framework.urls')),
    path('userlist/', UserListAPI.as_view()),
 ]