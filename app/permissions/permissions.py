from app.permissions.permission import Permission
from guest.permissions import is_guest

PERMISSIONS = [
    Permission(namespace="guest", permissions=[is_guest])

]
