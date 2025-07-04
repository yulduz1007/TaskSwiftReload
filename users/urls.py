from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import UserRegisterAPIView, UserGetMeView

urlpatterns = [
    path('user/create', UserRegisterAPIView.as_view()),
    path('user/login', TokenObtainPairView.as_view()),
    path('user/get-me', UserGetMeView.as_view()),
]