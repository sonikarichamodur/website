from django.contrib.auth.models import User
from django.db import models

from blog.models.post import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return '"{body}..." on {post_title} by {first_name} {last_name}'.format(body=self.body[:20],
                                                                  post_title=self.post.title,
                                                                  username=self.user.username,
                                                                  first_name=self.user.first_name,
                                                				  last_name=self.user.last_name,)
