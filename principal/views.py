from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from .models import Item, MenuItem


def index(request):
    user = request.user
    usuario = User.objects.get(username="rajiv")
    business = usuario.business
    menus = business.menu_set.all()
    for menu in menus:
        structure = menu.get_structure()

    return render_to_response('principal/index.html', {user: user}, context_instance=RequestContext(request))
