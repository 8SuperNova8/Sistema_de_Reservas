from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q, OuterRef, Exists, Case, When, Value, CharField
from apps.reservations.models import Reservation
from apps.rooms.serializers import AvailableRoomSerializer
from .models import Room
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class AvailableRoomsMixin:
    @extend_schema(
        parameters=[
            OpenApiParameter(name="room_type", type=OpenApiTypes.INT, required=True),
            OpenApiParameter(name="check_in", type=OpenApiTypes.DATE, description="YYYY-MM-DD", required=True),
            OpenApiParameter(name="check_out", type=OpenApiTypes.DATE, description="YYYY-MM-DD", required=True),
        ]
    )
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        serialicer = AvailableRoomSerializer(data=request.query_params)
        serialicer.is_valid(raise_exception=True)
        data = serialicer.validated_data

        #trae todos los Id de habitaciones que solapan con fechas 
        overlapping_dates = Reservation.objects.filter(
            room = OuterRef('pk'),
            check_in__lt = data['check_out'],
            check_out__gt = data['check_in'],
            status__in =[ 'confirmed', 'checked_in'] # __in es un lookup de Django que sirve para buscar valores dentro de una lista
        )

        #todas las habitaciones disponibles por tipo de habitacion 
        rooms = Room.objects.filter(
            room_type_id = data['room_type'],
        ).annotate(
            is_occupied = Exists(overlapping_dates)
        ).annotate(
            availability = Case(
                When(is_occupied = True, then=Value('occupied')),
                When(status = 'maintenance', then=Value('occupied')),
                When(status = 'inactive', then=Value('occupied')),
                default = Value('available'),
                output_field = CharField()
            )
        )

        return Response(rooms.values(
            'id',
            'room_number',
            'floor',
            'availability'
        ))

        