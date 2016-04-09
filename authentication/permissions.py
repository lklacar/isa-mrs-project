def is_logged_in(request):
    return request.user.is_authenticated()
