from django.conf import settings
from .models.nav import Nav
from .models.maintext import MainText
from .models.meeting import Meeting
from django.utils import timezone
from django.db.models import Q, Count


def heroku_info(request):
    return {
        'HEROKU_RELEASE_VERSION': settings.HEROKU_RELEASE_VERSION,
        'HEROKU_APP_NAME': settings.HEROKU_APP_NAME,
        'HEROKU_SLUG_COMMIT': settings.HEROKU_SLUG_COMMIT,
    }


def nav(request):
    return {
        'nav_items': Nav.objects.filter(parent=None).order_by("title").all(),
        'meetings': Meeting.objects.filter(start_time__lte=timezone.now()).filter(
            Q(end_time__isnull=True) | Q(end_time__gte=timezone.now())
        ).annotate(signins=Count('signins')).all(),
    }


def mains(request):
    return {
        'footer': MainText.objects.filter(text_type='Footer').order_by('pk').all(),
        'base_title': MainText.objects.filter(text_type='Base Title').order_by('pk').all(),
        'default_title': MainText.objects.filter(text_type='Default Title').order_by('pk').all(),
    }
