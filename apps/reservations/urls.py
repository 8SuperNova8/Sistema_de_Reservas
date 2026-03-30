from rest_framework import routers
from rest_framework.routers import DefaultRouter
from apps.reservations.views import ReservationViewSet, AdminReservationViewSet
from django.urls import path, include

router_public = DefaultRouter()
router_public.register ('reservations', ReservationViewSet, basename='public-resrevations')

router_admin = DefaultRouter()
router_admin.register(r'reservations', AdminReservationViewSet, basename='admin-reservations')

urlpatterns = [
    path('public/', include(router_public.urls)),
    path('admin/', include(router_admin.urls)),
]