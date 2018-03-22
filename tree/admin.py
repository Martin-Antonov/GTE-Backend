from django.contrib import admin

# Register your models here.
from tree.models import Tree


class TreeInline(admin.StackedInline):
    model = Tree
    readonly_fields = ('screenshot_url', )
    extra = 0

# admin.site.register(Tree, TreeAdmin)
