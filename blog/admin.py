from django.contrib import admin

from .models.comment import Comment
from .models.post import Post
from .models.nav import Nav
from .models.files import Files
from .models.meeting import Meeting
from .models.member import Member
from .models.signin import Signin
from .models.maintext import MainText
from django.db.models import F, Q, Sum
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import nested_admin
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


class NavInline(nested_admin.NestedStackedInline):
    model = Nav
    list_display = (
        'title',
        'user',
        'link',
        'pub_date',
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=False)


class NavAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        NavInline,
    ]
    exclude = [
        'parent',
    ]
    list_display = (
        'title',
        'user',
        'link',
        'pub_date',
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent=None)


class SigninInline(nested_admin.NestedStackedInline):
    model = Signin
    # readonly_fields = ('meeting',)
    raw_id_fields = ('meeting',)
    autocomplete_lookup_fields = {'fk': ('meeting',)}


class MemberAdmin(admin.ModelAdmin):
    inlines = [
        SigninInline,
    ]
    readonly_fields = ('hours', 'created', 'modified')
    fields = ('user', 'name', 'slack', 'created', 'modified', 'hours')
    list_display = (
        'name',
        'user',
        'slack',
        'hours',
    )

    def hours(self, obj):
        return list(Signin.objects.filter(user=obj).annotate(signin_time=F('end_time') - F('start_time')).aggregate(
            Sum('signin_time')).values())[0]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Nav, NavAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Files)
admin.site.register(MainText)

admin.site.register(Meeting)
admin.site.register(Signin)
admin.site.register(Member, MemberAdmin)
