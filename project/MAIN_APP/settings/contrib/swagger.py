from MAIN_APP.settings.environment import env

SPECTACULAR_SETTINGS = {
    'COMPONENT_SPLIT_REQUEST': True,
    'SWAGGER_UI_SETTINGS': {
        'persistAuthorization': True,
    },
}
SWAGGER_URL = env.str('SWAGGER_URL', None)
