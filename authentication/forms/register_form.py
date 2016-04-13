from django.contrib.auth.forms import UserCreationForm

from authentication.models import AbstractUser
from guest.models import Guest


class RegisterForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(RegisterForm, self).__init__(*args, **kargs)

    class Meta:
        model = Guest
        fields = ("email", "first_name", "last_name")

        error_messages = {
            'email': {
                'required': "You must enter a valid email address.",
                "unique": "There already exists a user with that email address",

            }
        }
