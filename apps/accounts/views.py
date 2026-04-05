from .serializers import UserAdminSerializer
from .models import User
from rest_framework import viewsets
from .permissions import IsSuperUser

class UserAdminViewSet(viewsets.ModelViewSet):
    serializer_class = UserAdminSerializer
    queryset = User.objects.all()
    permission_classes = [IsSuperUser]