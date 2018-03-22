import collections

from django.db import models

# Create your models here.
from django.utils import timezone
from jsonfield import JSONField

from users.models import GTEUser


class Tree(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    screenshot_url = models.CharField(max_length=512, blank=True, null=True)
    tree_json = JSONField(load_kwargs={"object_pairs_hook":collections.OrderedDict}, blank=True, null=True)
    user = models.ForeignKey(GTEUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title+ " " + str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year) +\
        "-" + str(self.date.hour) + ":" + str(self.date.minute)
