from django.contrib import admin

from blog.models.comment import Comment
from blog.models.post import Post
from blog.models.nav import Nav

admin.site.register(Nav)
admin.site.register(Post)
admin.site.register(Comment)
