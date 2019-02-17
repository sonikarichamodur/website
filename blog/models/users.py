from django.contrib.auth.models import User
from django.db import models


class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, verbose_name="Display Name")
