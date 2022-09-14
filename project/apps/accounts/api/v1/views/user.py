from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, permissions

from apps.accounts.api.v1.serializers.user import UserSerializer

User = get_user_model()


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
