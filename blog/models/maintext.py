from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class MainText(models.Model):
    TEXT_TYPE_CHOICES = (
        ('Draft', 'Draft'),
        ('Main Page', 'Main'),
        ('Footer', 'Footer'),
        ('Base Title', 'Base Title'),
        ('Default Title', 'Default Title'),
    )
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    text_type = models.CharField(max_length=254, default='Draft', choices=TEXT_TYPE_CHOICES)

    def __str__(self):
        return f'{self.text_type}={self.pk}'
