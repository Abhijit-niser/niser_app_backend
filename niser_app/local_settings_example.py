# Search for tags "<...>" and replace them with your own values also rename this file to "local_settings.py"

debug = False
SECRET_KEY = '<your django secret key>'
IP = "<serverIP>"  # e.g.: 127.0.0.1
PORT = "<serverPort>"  # e.g.: 8000
PROTOCOL = "http"  #  http/https
DOMAIN = f"{PROTOCOL}://{IP}:{PORT}"

AUTH_USER_MODEL = 'authtools.User'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<server email addres>'
EMAIL_HOST_PASSWORD = '<your 16 digit password generated in google account in the App Passwords section>'
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'NISER App'

SERVICE_JSON = '<path to your firebase service json>.json'  # for example view .gitignore file

NOTIFICATION_TOKEN_FILE = "tokens.json"


# Celery settings

CELERY_BROKER_URL = 'redis://127.0.0.1:6379'  # <...> might need to change
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'  # <...> might need to change
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = CELERY_RESULT_SERIALIZER


import firebase_admin
# put your own project name
access_token_object = firebase_admin.initialize_app().credential.get_access_token()
NOTIFICATION_REQUEST_URL = "https://fcm.googleapis.com/v1/projects/<project name in firebase>/messages:send"
NOTIFICATION_REQUEST_HEADER = {
    'Authorization': 'Bearer ' + access_token_object.access_token,
    'Content-Type': 'application/json; UTF-8',
}

