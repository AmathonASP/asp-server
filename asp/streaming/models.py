from django.db import models

# Create your models here.
class Audio(models.Model):
    thumbnail = models.ImageField()
    artist = models.CharField(default=None, max_length=32, null=True, blank=True)
    title = models.CharField(default=None, max_length=64, null=True, blank=True)
