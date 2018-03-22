from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models


class GeneralInformation(models.Model):
    home_title = models.CharField(max_length=255)
    home_information = RichTextField()
    home_video_file = models.FileField()

    docs_title = models.CharField(max_length=255)
    docs_information = RichTextField()

    about_GTE_title = models.CharField(max_length=255)
    about_GTE_information = RichTextField()
    about_contributors_title = models.CharField(max_length=255)
    # about_contributors_information = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    about_publications_title = models.CharField(max_length=255)
    # about_publications_information = models.ForeignKey(Publication, on_delete=models.CASCADE)

    def validate_only_one_instance(obj):
        model = obj.__class__
        if (model.objects.count() > 0 and
                    obj.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)

    def clean(self):
        self.validate_only_one_instance()

    def __str__(self):
        return self.home_title


class Contributor(models.Model):
    general_information_contributor = models.ForeignKey(GeneralInformation, on_delete=models.DO_NOTHING)
    text = RichTextField()

    def __str__(self):
        initial_text = str(self.text)
        if initial_text.__contains__(">"):
            final_text = initial_text[initial_text.find('>'):initial_text.find('</')]
        else:
            final_text = initial_text
        return final_text


class Publication(models.Model):
    general_information_publication = models.ForeignKey(GeneralInformation, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default="")
    text = RichTextField()

    def __str__(self):
        return self.title


class Documentation(models.Model):
    docs_json = models.FileField(null=True)

    def __str__(self):
        return "JSON Docs"

