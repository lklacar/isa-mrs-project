import datetime

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from authentication.models import ConfirmationToken


@require_http_methods(["GET"])
def confirm(request):
    token = request.GET['token']

    try:
        confirmation_token = ConfirmationToken.objects.get(token=token)
    except:
        raise Exception("Invalid confirmation token")

    if confirmation_token.expires < datetime.datetime.now():
        raise Exception("Confirmation token expired")

    user = confirmation_token.user
    user.is_confirmed = True
    user.save()

    return HttpResponse("Confirmed")
