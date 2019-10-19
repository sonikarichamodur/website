from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
import logging
from blog.models.users import Details
from blog.models.post import Post
from blog.models.member import Member
from blog.models.meeting import Meeting

base_log = logging.getLogger('blog.models.signin')


class Signin(models.Model):
    def meetingValidator(signin):
        log = base_log.getChild("meetingValidator")
        log.debug("In meeting validator", extra=dict(signin=signin))
        ret = signin.meeting and signin.user and Signin.objects.filter(
            user=signin.user,
            meeting=signin.meeting,
            start_time__isnull=False,
            end_time__isnull=True,
        ).count() == 0
        log.debug("End meeting validator", extra=dict(signin=signin, ret=ret))
        return ret

    def startValidator(signin):
        if signin.start_time is not None:
            return signin.start_time < timezone.now()
        return True

    def endValidator(signin):
        if signin.end_time is not None:
            return signin.end_time > timezone.now()
        return True

    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=False, validators=[meetingValidator, ])
    start_time = models.DateTimeField('sign-in time', auto_now_add=True, null=False, validators=[startValidator, ])
    end_time = models.DateTimeField('sign-out time', null=True, validators=[endValidator, ])

    def __str__(self):
        return "{user} signed in to {meeting} from {start_time} to {end_time}".format(user=self.user.name,
                                                                                      start_time=self.start_time,
                                                                                      end_time=self.end_time,
                                                                                      meeting=self.meeting.start_time, )
