from django.conf import settings


def heroku_info(request):
    return {
        'HEROKU_RELEASE_VERSION': settings.HEROKU_RELEASE_VERSION,
        'HEROKU_APP_NAME': settings.HEROKU_APP_NAME,
        'HEROKU_SLUG_COMMIT': settings.HEROKU_SLUG_COMMIT,
    }
