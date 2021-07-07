from django.db import models
from django.conf import settings


class Publicacao(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=200, null=False)
