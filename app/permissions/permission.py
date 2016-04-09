class Permission(object):
    def __init__(self, namespace="", url_name="", view_name="", permissions=None):
        if permissions is None:
            permissions = []

        self.namespace = namespace
        self.url_name = url_name
        self.view_name = view_name
        self.permissions = permissions

    def has_permission(self, request):
        for permission in self.permissions:
            if not permission(request):
                return False

        return True
