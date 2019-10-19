from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from blog.models.users import Details
from blog.models.post import Post
from blog.models.member import Member
from blog.models.meeting import Meeting


def startValidator(signin):
    if signin.start_time is not None:
        return signin.start_time < timezone.now()

    return True


def endValidator(signin):
    if signin.end_time is not None:
        return signin.end_time > timezone.now()

    return True


class Signin(models.Model):
    def meetingValidator(signin):
        if signin.meeting is not None:
            return Signin.objects.filter(
                user=signin.user,
                meeting=signin.meeting,
                start_time__isnull=False,
                end_time__isnull=True,
            ).count() == 0

        return True

    user = models.ForeignKey(Member, on_delete=models.CASCADE, null=False)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=False, validators=[meetingValidator, ])
    start_time = models.DateTimeField('sign-in time', auto_now_add=True, null=False, validators=[startValidator, ])
    end_time = models.DateTimeField('sign-out time', null=True, validators=[endValidator, ]),

    #
    # def clean(self):
    #     # Not really needed
    #     super().clean()
    #
    #     # Skip this if self.meeting isn't defined yet
    #     try:
    #         if Signin.objects.filter(
    #                 user=self.user,
    #                 meeting=self.meeting,
    #                 start_time__isnull=False,
    #                 end_time__isnull=True,
    #         ).count() > 0:
    #             raise ValidationError("User already signed in")
    #     except Signin.meeting.RelatedObjectDoesNotExist as e:
    #         pass
    #
    #     if not startValidator(self):
    #         raise ValidationError("Invalid start time")
    #
    #     if not endValidator(self):
    #         raise ValidationError("User didn't sign out")

    def __str__(self):
        return "{user} signed in to {meeting} from {start_time} to {end_time}".format(user=self.user.name,
                                                                                      start_time=self.start_time,
                                                                                      end_time=self.end_time,
                                                                                      meeting=self.meeting.start_time, )
