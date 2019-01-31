from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    fil = models.BinaryField(max_length=1024 ^ 3)
    filepath = models.SlugField(max_length=32)
    ext = models.SlugField(max_length=8)

    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:files', kwargs={'pk': self.pk})

    def __str__(self):
        return '"{title}" by {username}'.format(title=self.title,
                                                username=self.user.username)
