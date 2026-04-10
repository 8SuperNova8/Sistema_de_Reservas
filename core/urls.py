from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/', include('apps.rooms.urls')),
    path('api/', include('apps.reservations.urls')),
    path('api/', include('apps.payments.urls')),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/', include('apps.accounts.urls'))
    

]
