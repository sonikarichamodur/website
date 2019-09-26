from django.contrib.auth.models import User
from django.db import models
from djanbo.utils import timezone
from blog.models.users import Details
from blog.models.post import Post


class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('meeting start time', auto_now_add=True, editable=True)
    end_time = models.DateTimeField('meeting end time', default=timezone.now, null=True)

    def __str__(self):
        return "meeting from {start_time} to {end_time}".format(start_time=self.start_time, end_time=self.end_time)

    class Meta:
        permissions = (
            ("meeting_gui_can_create", "Can create new meetings via the GUI"),
        )
