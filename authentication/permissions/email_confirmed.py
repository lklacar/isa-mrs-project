from django.http import HttpResponse


def is_email_confirmed(function):
    """
    Works only if user is already logged in !!!
    :param function:
    :return:
    """

    def wrap(request, *args, **kwargs):
        if not request.user.is_confirmed():
            return HttpResponse("You must confirm your email first.")

        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
