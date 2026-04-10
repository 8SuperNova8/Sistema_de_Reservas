from rest_framework.routers import DefaultRouter
from .views import UserAdminViewSet

router = DefaultRouter()
router.register('admin', UserAdminViewSet, basename='administrator')

urlpatterns = router.urls