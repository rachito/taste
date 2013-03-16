from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    user = request.user
    business = user.business
    menus = business.menu_set.all()

    return render_to_response(
        'principal/index.html',
        {'menus':menus},
        context_instance=RequestContext(request)
    )
