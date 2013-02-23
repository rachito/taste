from django.shortcuts import render_to_response
from django.template import RequestContext
from principal.models import User, Menu


def index(request):
    business = User.objects.get(id=1).business
    m = Menu.objects.get(id=1)

    return render_to_response(
        'principal/index.html',
        {'business': business},
        context_instance=RequestContext(request)
    )
