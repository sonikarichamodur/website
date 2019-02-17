from django.contrib import admin

from .models.comment import Comment
from .models.post import Post
from .models.nav import Nav
from .models.files import Files
from .models.maintext import MainText
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models.users import Details


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class DetailsInline(admin.StackedInline):
    model = Details
    can_delete = False
    verbose_name_plural = 'details'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (DetailsInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Nav)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Files)
admin.site.register(MainText)
