from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# from tree.models import Tree


class GTEUser(AbstractUser):
    # trees = models.ForeignKey(Tree, on_delete=models.CASCADE, null=True)
    institution = models.CharField(max_length=255, blank=True, null=True)
    pass
