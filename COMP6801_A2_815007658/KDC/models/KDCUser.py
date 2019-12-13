from django.db import models
from django.utils import timezone

import uuid


class KDCUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField()

    class Meta:
        ordering = ['username']

    def __str__(self):
        return '{0}'.format(self.username)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        return super(KDCUser, self).save(*args, **kwargs)
