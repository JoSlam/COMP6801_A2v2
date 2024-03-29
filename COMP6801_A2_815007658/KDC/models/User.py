from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from KDC.models.UserManager import UserManager
from TGS.models.Application import Application


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    applications = models.ManyToManyField(to=Application, through="UserApplication")

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class UserApplication(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    application = models.ForeignKey(to=Application, on_delete=models.CASCADE)
    nonce = models.TextField()
    tgt = models.TextField(verbose_name="Ticket granting ticket")