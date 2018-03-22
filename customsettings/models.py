from django.db import models

# Create your models here.
from users.models import GTEUser


class CustomSettings(models.Model):
    user = models.ForeignKey(GTEUser, null=True, on_delete=models.CASCADE)
    tree_width = models.FloatField(default=0.0, blank=True)
    tree_height = models.FloatField(default=0.0, blank=True)
