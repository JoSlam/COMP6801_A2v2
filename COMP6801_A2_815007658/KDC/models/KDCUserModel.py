from django.db import models
from django.utils import timezone

import uuid


class KDCUserModel(model.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date_created = models.DateTimeField()

    def __str__(self):
        return '{0}'.format(self.username)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        self.username = username
        self.password = password
        return super(KDCUserModel, self).save(*args, **kwargs)
