from app.permissions.permission import Permission
from guest.permissions import is_guest


def is_manager(request):
    if not request.user.is_authenticated() or request.user.is_anonymous():
        return False

    return request.user.role == "MANAGER"


def is_system_manager(request):
    if not request.user.is_authenticated() or request.user.is_anonymous():
        return False

    return request.user.role == "SYSTEM_MANAGER"


PERMISSIONS = [
    Permission(namespace="guest", permissions=[is_guest]),
    Permission(namespace="manager", permissions=[is_manager]),
    Permission(namespace="system_manager", permissions=[is_system_manager]),

]
