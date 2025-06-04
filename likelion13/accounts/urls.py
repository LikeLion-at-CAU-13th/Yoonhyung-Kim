from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    
    path("join/", RegisterView.as_view()),
    path("login/", AuthView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("google/login/", google_login, name="google_login"), # 프론트 협업 시 삭제
    path("google/callback/", google_callback, name="google_callback")
]