from django.contrib import admin

from .models.comment import Comment
from .models.post import Post
from .models.nav import Nav
from .models.files import Files

admin.site.register(Nav)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Files)
