from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager as DjBaseUserManager)

from model_utils.managers import InheritanceManager

from django.utils.translation import ugettext_lazy as _


class BaseUserManager(DjBaseUserManager, InheritanceManager):
    """
    Manager for all Users types
    create_user() and create_superuser() must be overriden as we do not use
    unique username but unique email.
    """

    def create_user(self, email=None, password=None, **extra_fields):
        now = timezone.now()
        email = BaseUserManager.normalize_email(email)
        u = GenericUser(email=email, is_superuser=False, last_login=now,
                        **extra_fields)
        u.set_password(password)
        u.save(using=self._db)
        return u

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_superuser = True
        u.save(using=self._db)
        return u


class CallableUser(AbstractBaseUser):
    """
    The CallableUser class allows to get any type of user by calling
    CallableUser.objects.get_subclass(email="my@email.dom") or
    CallableUser.objects.filter(email__endswith="@email.dom").select_subclasses()
    """
    objects = BaseUserManager()


class AbstractUser(CallableUser):
    """
    Here are the fields that are shared among specific User subtypes.
    Making it abstract makes 1 email possible in each User subtype.
    """
    email = models.EmailField(unique=True)
    is_superuser = False
    objects = BaseUserManager()
    is_confirmed = models.BooleanField(default=False)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    def __unicode__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = USERNAME_FIELD

    class Meta:
        abstract = True


class GenericUser(AbstractUser):
    """
    A GenericUser is any type of system user (such as an admin).
    This is the one that should be referenced in settings.AUTH_USER_MODEL
    """
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class ConfirmationToken(models.Model):
    user = models.OneToOneField(GenericUser)
    token = models.CharField(max_length=36)
    expires = models.DateTimeField()
