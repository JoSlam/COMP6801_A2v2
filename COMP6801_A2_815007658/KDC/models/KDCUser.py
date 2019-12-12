from django.db import models
from django.utils import timezone

import uuid


class KDCUser(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField()

    class Meta:
        ordering = ['username']

    def __str__(self):
        return '{0}'.format(self.username)

    def save(self, *args, **kwargs):
        if not self.uid:
            self.date_created = timezone.now()
        self.username = username
        self.password = password
        return super(KDCUser, self).save(*args, **kwargs)
