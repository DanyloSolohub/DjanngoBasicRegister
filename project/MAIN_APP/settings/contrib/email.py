from MAIN_APP.settings.environment import env

EMAIL_BACKEND = 'django_ses.SESBackend'

DEFAULT_FROM_EMAIL = env.str('DEFAULT_FROM_EMAIL')
AWS_SES_ACCESS_KEY_ID = env.str('AWS_SES_ACCESS_KEY_ID', None)
AWS_SES_SECRET_ACCESS_KEY = env.str('AWS_SES_SECRET_ACCESS_KEY', None)
AWS_SES_REGION_NAME = env.str('AWS_SES_REGION_NAME', 'eu-central-1')
AWS_SES_REGION_ENDPOINT = env.str('AWS_SES_REGION_ENDPOINT', 'email.eu-central-1.amazonaws.com')
