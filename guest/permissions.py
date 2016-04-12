def is_guest(request):
    return request.user.is_authenticated() and request.user.role == "GUEST"
