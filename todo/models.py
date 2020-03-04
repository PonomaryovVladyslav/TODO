from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Notes(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Zametka'
        verbose_name_plural = 'Zametki'