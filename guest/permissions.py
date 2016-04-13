from guest.models import Guest


def is_guest(request):
    user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user

    return request.user.is_authenticated() and type(user) == Guest
