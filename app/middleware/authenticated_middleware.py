from django.http import HttpResponseForbidden

from app.permissions.permissions import PERMISSIONS
from guest.models import Guest


class AuthenticatedMiddleware(object):
    def process_response(self, request, response):
        if request.resolver_match is None:
            return response

        user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user
        if type(user) == Guest and not user.is_confirmed:
            return HttpResponseForbidden("You must confirm your email first.")

        for permission in PERMISSIONS:
            resolver_match = request.resolver_match
            if resolver_match.namespace == permission.namespace or resolver_match.url_name == permission.url_name or resolver_match.view_name == permission.view_name:
                if permission.has_permission(request):
                    return response
                else:

                    return HttpResponseForbidden("You have no permission to access this page")

        return response
