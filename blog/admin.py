from django.contrib import admin

from .models.comment import Comment
from .models.post import Post
from .models.nav import Nav
from .models.files import Files
from .models.maintext import MainText

admin.site.register(Nav)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Files)
admin.site.register(MainText)
