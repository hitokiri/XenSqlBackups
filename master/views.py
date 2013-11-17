from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def vista_index(request):
	return render_to_response('index.html', context_instance = RequestContext(request))

def vista_login(request):
	return render_to_response('login.html', context_instance = RequestContext(request))