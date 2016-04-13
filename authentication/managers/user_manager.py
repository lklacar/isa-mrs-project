from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager as DjBaseUserManager)
from model_utils.managers import InheritanceManager


class UserManager(DjBaseUserManager, InheritanceManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()

        # Neither Facebook nor Twitter provide us with user's email address, so we will use their username instead
        if email != "":
            email = self.normalize_email(email)
        else:
            email = extra_fields['username']

        if "username" in extra_fields.keys():
            del extra_fields['username']

        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)
