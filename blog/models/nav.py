from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Nav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    link = models.SlugField(max_length=10)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    parent = models.ForeignKey('Nav', null=True, default=None, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})

    def __str__(self):
        return '"{title}" by {name}'.format(title=self.title,
                                            name=self.user.details.display() if self.user.details else self.user.first_name)
