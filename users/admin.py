from django.contrib import admin

# Register your models here.
from tree.admin import TreeInline
from users.models import GTEUser


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)
    exclude = ('groups', 'user_permissions', 'is_active', )
    inlines = [TreeInline,]


admin.site.register(GTEUser, UserAdmin)