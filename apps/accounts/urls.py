from django.urls import path
from .views import RegisterAPIView,ProfileAPIView
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView)



urlpatterns = [
    path("auth/register/",RegisterAPIView.as_view(),name="register",),
    path("profile/",ProfileAPIView.as_view(),name="profile"),

    path("login/",TokenObtainPairView.as_view(),name="login"),
    path("refresh",TokenRefreshView.as_view(),name="refresh"),
]