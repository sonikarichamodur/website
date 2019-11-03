from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from blog.models.users import Details
from blog.models.post import Post
from django.db.models import Q
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords


def start_validator(meeting):
    if meeting.start_time is not None:
        return meeting.start_time < timezone.now()

    return True


def end_validator(meeting):
    if meeting.end_time is not None:
        return meeting.end_time <= timezone.now()

    return True


class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('meeting start time', auto_now_add=True, editable=True)
    end_time = models.DateTimeField('meeting end time', default=None, null=True, blank=True)
    history = HistoricalRecords()

    def clean(self):
        base_filter = Meeting.objects.filter(
            start_time__lte=timezone.now(),
        ).filter(
            Q(end_time__isnull=True) | Q(end_time__gte=timezone.now())
        )

        # If we already have a pk then filter us out from the count
        if self.id:
            base_filter = base_filter.filter(~Q(id=self.id))

        if base_filter.count() > 0:
            raise ValidationError("cannot create multiple meetings")
        if not start_validator(self):
            raise ValidationError("cannot create meeting")

        if not end_validator(self):
            raise ValidationError("cannot create meeting")

    def __str__(self):
        return "meeting from {start_time} to {end_time}".format(start_time=self.start_time, end_time=self.end_time)

    class Meta:
        permissions = (
            ("meeting_gui_can_create", "Can create new meetings via the GUI"),
        )
