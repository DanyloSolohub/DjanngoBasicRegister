from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularJSONAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/v1/accounts/', include('apps.accounts.api.v1.urls'))
]
if settings.SWAGGER_URL:
    urlpatterns += [
        path('api/v1/_schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/v1/_schema.json', SpectacularJSONAPIView.as_view(), name='schema'),
        path(f'{settings.SWAGGER_URL}', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    ]
