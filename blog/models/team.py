from django.db import models
import logging
from simple_history.models import HistoricalRecords

base_log = logging.getLogger('blog.models.signin')


class Team(models.Model):
    name = models.CharField(max_length=255, primary_key=True, editable=False, null=False, blank=False)
    display_name = models.CharField(max_length=255, unique=True, null=False, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.display_name
