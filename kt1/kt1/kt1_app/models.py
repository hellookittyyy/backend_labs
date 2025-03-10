from django.db import models

class Url(models.Model):
    url = models.URLField()
    shortCode = models.CharField(max_length=10, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    accessCount = models.IntegerField(default=0)
