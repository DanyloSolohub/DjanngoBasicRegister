from django.conf import settings

from apps.accounts.models import User
from apps.accounts.tasks.email import send_email
from django.core.mail import send_mail


class EmailServices:

    @staticmethod
    def email_user_creation(user: User, password: str) -> bool:
        email_dict = {
            'title': 'Account creation',
            'password': password,
        }
        send_email.s(
            email=user.email,
            title='Account creation',
            template_name='email_user_creation.html',
            data_for_template=email_dict,
        ).apply_async()
        return True
