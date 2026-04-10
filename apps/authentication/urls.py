from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import change_password

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='email_login'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password', change_password, name='change_password_login')
]