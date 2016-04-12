from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

from authentication.managers.user_manager import UserManager
from restaurant_booking import settings


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_confirmed = models.BooleanField(_('email confirmed'), default=False,
                                       help_text=_('Designates whether the user confirmed his/her email'))

    objects = UserManager()

    CHOICES = (
        ("GUEST", 'Guest'),
        ("MANAGER", 'Manager'),
        ("SYSTEM_MANAGER", 'System manager'),
        ("WAITER", 'Waiter'),
        ("CHEF", 'Chef'),
        ("BARTENDER", 'Bartender'),
    )
    role = models.CharField(max_length=20,
                            choices=CHOICES,
                            default="GUEST")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def send_email(self, subject, message):
        send_mail(subject, message, settings.EMAIL_HOST_USER, [self.email])

    def permissions(self):
        return Permission.objects.filter(user=self)
