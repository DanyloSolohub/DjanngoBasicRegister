from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from apps.accounts.services.email import EmailServices
from apps.accounts.services.user import UserServices

User = get_user_model()


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

    def create(self, validated_data):
        user = super().create(validated_data)
        password = UserServices.set_and_get_password(user)
        EmailServices.email_user_creation(user, password)
        return user
