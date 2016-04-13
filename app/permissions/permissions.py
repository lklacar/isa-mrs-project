from app.permissions.permission import Permission
from guest.permissions import is_guest
from manager.models import Manager
from system_manager.models import SystemManager


def is_manager(request):
    user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user

    if not request.user.is_authenticated() or request.user.is_anonymous():
        return False

    return type(user) == Manager


def is_system_manager(request):
    user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user
    if not request.user.is_authenticated() or request.user.is_anonymous():
        return False

    return type(user) == SystemManager


PERMISSIONS = [
    Permission(namespace="guest", permissions=[is_guest]),
    Permission(namespace="manager", permissions=[is_manager]),
    Permission(namespace="system_manager", permissions=[is_system_manager]),

]
