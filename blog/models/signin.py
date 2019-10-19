from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q, F
from django.utils import timezone
import logging
from blog.models.users import Details
from blog.models.post import Post
from blog.models.member import Member
from blog.models.meeting import Meeting

base_log = logging.getLogger('blog.models.signin')


class Signin(models.Model):
    def startValidator(value):
        if value is not None:
            return value < timezone.now()
        return True

    def endValidator(value):
        if value is not None:
            return value > timezone.now()
        return True

    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=False)
    start_time = models.DateTimeField('sign-in time', auto_now_add=True, null=False, validators=[startValidator])
    end_time = models.DateTimeField('sign-out time', null=True, validators=[endValidator])

    def __str__(self):
        return "{user} signed in to {meeting} from {start_time} to {end_time}".format(user=self.user.name,
                                                                                      start_time=self.start_time,
                                                                                      end_time=self.end_time,
                                                                                      meeting=self.meeting.start_time,
                                                                                      )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="user_meeting_chk",
                fields=[
                    "user",
                    "meeting",
                ],
                condition=Q(
                    end_time__isnull=True,
                )
            )
        ]
