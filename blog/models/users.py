from django.contrib.auth.models import User
from django.db import models


class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, verbose_name="Display Name")

    def display(self):
        if self.display_name:
            return self.display_name
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + " " + self.user.last_name[0]
        if self.user.first_name:
            return self.user.first_name
        return self.user.username

    @classmethod
    def name(cls, user):
        try:
            return user.details.display()
        except models.RelatedObjectDoesNotExist:
            if user.first_name and user.last_name:
                return user.first_name + " " + user.last_name[0]
            if user.first_name:
                return user.first_name
            return user.username
