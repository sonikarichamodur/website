from django.contrib.auth.models import User
from django.db import models
from blog.models.users import Details
from blog.models.post import Post


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField('member name', max_length=4096)
    slack = models.CharField('slack id', max_length=4096)
    created = models.DateTimeField('user added', auto_now_add=True)
    modified = models.DateTimeField('user modified', auto_now=True)

    def __str__(self):
        return "{name}".format(name=self.name)
