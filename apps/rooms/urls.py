from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router_public = DefaultRouter()
router_public.register ('rooms', views.RoomViewSet, basename='public-room')
router_public.register (r'room-types', views.RoomTypeViewSet, basename='public-roomType')

router_admin = DefaultRouter()
router_admin.register(r'room-types', views.RoomTypeAdminViewset, basename='admin-roomType' )
router_admin.register('rooms', views.RoomAdminViewSet, basename='admin-room' )

urlpatterns = [
    path('public/', include(router_public.urls)),
    path('admin/', include(router_admin.urls)),
]