from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    text              = models.TextField(blank=False)
    title             = models.CharField(max_length=200,default="No Title")
    publication_date  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

