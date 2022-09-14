from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from MAIN_APP import celery_app


@celery_app.task
def send_email(email: str, title: str, template_name: str, data_for_template: dict) -> bool:
    subject, to = title, email
    html_message = render_to_string(template_name, data_for_template)
    message = EmailMultiAlternatives(
        subject=subject,
        body=html_message,
        to=[to],
    )
    message.mixed_subtype = 'related'
    message.attach_alternative(html_message, 'text/html')
    message.send(fail_silently=True)
    return True
