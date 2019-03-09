from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import mimetypes
from blog.models.users import Details


class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Owner")
    title = models.CharField(max_length=80, verbose_name="Title")
    fil = models.FileField(verbose_name="File")
    pub_date = models.DateTimeField(verbose_name='date published', auto_now_add=True)

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

    def get_rel_url(self):
        return "/files/%s.%s" % (
            self.pk, self.get_ext(),
        )

    def get_update_url(self):
        return reverse('blog:update_file', kwargs={'pk': self.pk, 'ext': self.get_ext()})

    def get_delete_url(self):
        return reverse('blog:delete_file', kwargs={'pk': self.pk, 'ext': self.get_ext()})

    class Meta:
        permissions = (
            ("files_gui_own_create", "Can upload files via the GUI"),
            ("files_gui_own_delete", "Can delete their own files via the GUI"),
            ("files_gui_own_update", "Can update their own files via the GUI"),
            ("files_gui_own_list", "Can view their own list of files via the GUI"),
            ("files_gui_all_delete", "Can delete all user's files via the GUI"),
            ("files_gui_all_update", "Can update all user's files via the GUI"),
            ("files_gui_all_list", "Can view all user's list of files via the GUI"),
        )
        verbose_name = "File"
        verbose_name_plural = "Files"
