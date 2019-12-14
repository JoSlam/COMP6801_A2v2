from . import *
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password, MD5PasswordHasher


class UserManager(BaseUserManager):
    salt = "1234"
    hash_algo = MD5PasswordHasher

    def create_user(self, username, email=None, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError('Users must have a username')
        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model()
        user_obj.username = username
        user_obj.password = make_password(password, salt=self.salt, hasher='default')
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.date_created = timezone.now()

        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
            is_staff=True,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
            is_admin=True,
            is_staff=True
        )
        user.save(using=self._db)
        return user