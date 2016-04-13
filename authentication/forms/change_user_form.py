from django.contrib.auth.forms import UserChangeForm

from authentication.models import AbstractUser
from authentication.models.default_user import DefaultUser


class ChangeUserForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(ChangeUserForm, self).__init__(*args, **kargs)

    class Meta:
        model = DefaultUser
        fields = ['email', 'password']
