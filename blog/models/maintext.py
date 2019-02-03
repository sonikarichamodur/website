from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class MainText(models.Model):
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
