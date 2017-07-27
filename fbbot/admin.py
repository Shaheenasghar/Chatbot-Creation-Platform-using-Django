
# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from fbbot.models import FBUser, Partner

admin.site.register(Partner)


class FBUserInline(admin.StackedInline):
    model = FBUser
    can_delete = False
    verbose_name_plural = 'facebook_user'


class UserAdmin(BaseUserAdmin):
    inlines = (FBUserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


