from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import mimetypes


class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    fil = models.FileField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:download_file', kwargs={'pk': self.pk})

    def __str__(self):
        return '"{title}" by {username}'.format(title=self.title,
                                                username=self.user.username)

    def get_s3_url(self):
        return self.fil.url

    def get_content_type(self):
        return mimetypes.guess_type(self.fil.name) or 'application/octet-stream'
