from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
#from .views import EmailTokenObtainView

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='email_login'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh')
]