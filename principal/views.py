from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import User, Menu


def index(request):
    return render_to_response('principal/index.html', {}, context_instance=RequestContext(request))
