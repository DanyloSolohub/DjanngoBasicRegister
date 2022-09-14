from random import randint

from django.contrib.auth import get_user_model

User = get_user_model()


class UserServices:

    @staticmethod
    def generate_password(len_password=8):
        symbols = [chr(randint(40, 126)) for _ in range(len_password)]
        return ''.join(symbols)

    @classmethod
    def set_and_get_password(cls, user: User, len_password=8) -> str:
        password = cls.generate_password(len_password)
        user.set_password(password)
        user.save(update_fields=['password'])
        return password
