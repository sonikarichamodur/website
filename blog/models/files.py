from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import mimetypes
from blog.models.users import Details


class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    fil = models.FileField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_ext(self):
        return self.fil.name.split('.')[-1]

    def get_absolute_url(self):
        # Handle no extension files
        return reverse('blog:download_file', kwargs={'pk': self.pk, 'ext': self.get_ext()})

    def __str__(self):
        return '"{title}" by {name}'.format(title=self.title,
                                            name=Details.name(self.user))

    def get_s3_url(self):
        return self.fil.url

    def get_content_type(self):
        return mimetypes.guess_type(self.fil.name) or 'application/octet-stream'

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

    def get_rel_url(self):
        return "/files/%s.%s" % (
            self.pk, self.get_ext(),
        )
