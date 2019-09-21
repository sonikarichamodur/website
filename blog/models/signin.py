from django.contrib.auth.models import User
from django.db import models
from blog.models.users import Details
from blog.models.post import Post
from blog.models.member import Member
from blog.models.meeting import Meeting


class Signin(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    start_time = models.DateTimeField('sign-in time', auto_now_add=True)
    end_time = models.DateTimeField('sign-out time', null=True)

    def __str__(self):
        return "{user} signed in from {start_time} to {end_time}".format(user=self.user.username,
                                                                         start_time=self.start_time,
                                                                         end_time=self.end_time)
