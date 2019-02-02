from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class MainText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    link = models.SlugField(max_length=10)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
