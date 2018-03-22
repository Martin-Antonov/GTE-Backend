from django.contrib import admin

from general_information.models import GeneralInformation, Contributor, Publication, Documentation


class ContributorsInline(admin.StackedInline):
    model = Contributor
    extra = 1


class PublicationsInline(admin.StackedInline):
    model = Publication
    extra = 1


class GeneralInformationAdmin(admin.ModelAdmin):
    inlines = [ContributorsInline, PublicationsInline, ]



admin.site.register(GeneralInformation, GeneralInformationAdmin)
admin.site.register(Documentation)

