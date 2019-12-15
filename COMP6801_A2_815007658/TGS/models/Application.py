from django.db import models
from django.utils import timezone

from uuid import uuid4
from KDC.models import User


class Application(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name="Application Name")
    key = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name="Application Key")
    date_created = models.DateTimeField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = timezone.now()
        super(Application, self).save(*args, **kwargs)
