from rest_framework import viewsets, status, mixins
from datetime import datetime
from apps.rooms.models import Room, RoomType
from apps.rooms.serializers import RoomSerializer, RoomTypeSerializer
from .mixins import AvailableRoomsMixin

#Perfil Publico
class RoomTypeViewSet (
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()

class RoomViewSet (
    viewsets.GenericViewSet,
    AvailableRoomsMixin
    ):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

#***************************

#permisos para Admin
class RoomTypeAdminViewset (viewsets.ModelViewSet):
    serializer_class= RoomTypeSerializer
    queryset = RoomType.objects.all()

    
class RoomAdminViewSet(
    viewsets.ModelViewSet,
    AvailableRoomsMixin
    ):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()