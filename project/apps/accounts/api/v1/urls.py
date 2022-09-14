from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.accounts.api.v1.views.register import RegisterView
from apps.accounts.api.v1.views.user import UserViewSet

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', UserViewSet.as_view({'get': 'retrieve', 'patch': 'update'}))
]
