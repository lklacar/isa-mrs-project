from django.shortcuts import redirect


class AuthenticatedMiddleware(object):
    def process_response(self, request, response):
        if ("/auth/" not in request.path and "social" not in request.path) and request.user.is_authenticated() == False:
            return redirect("auth:login-or-register")

        return response
