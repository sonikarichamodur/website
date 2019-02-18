from django.conf import settings
from blog.models.nav import Nav


def heroku_info(request):
    return {
        'HEROKU_RELEASE_VERSION': settings.HEROKU_RELEASE_VERSION,
        'HEROKU_APP_NAME': settings.HEROKU_APP_NAME,
        'HEROKU_SLUG_COMMIT': settings.HEROKU_SLUG_COMMIT,
    }


def nav(request):
    return {
        'nav_items': Nav.objects.filter(parent=None).order_by("title").all(),
    }
