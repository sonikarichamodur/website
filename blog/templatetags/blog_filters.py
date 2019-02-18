from django import template
from datetime import date, timedelta
from django.contrib.auth.models import User
from blog.models.users import Details

register = template.Library()


@register.filter(name='human_name')
def human_name(value):
    try:
        user = User.objects.get(pk=value)
        return Details.name(user)
    except User.DoesNotExist:
        return None
