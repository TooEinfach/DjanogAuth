from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Files(models.Model):
    json_file = models.FileField(upload_to='json/')
    datestamp = models.DateTimeField(auto_now_add=True)
