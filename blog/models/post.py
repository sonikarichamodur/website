from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from blog.models.users import Details


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})

    def __str__(self):
        return '"{title}" by {name}'.format(
            title=self.title,
            name=Details.name(self.user),
        )

    class Meta:
        permissions = (
            ("post_gui_can_post", "Can create new posts via the GUI"),
            ("post_gui_can_update", "Can update own posts via the GUI"),
            ("post_gui_can_delete", "Can delete own posts via the GUI"),
        )
