#coding:utf-8
from master.models import DatosHost
from django.http import HttpResponseRedirect


def datos_decorator(funcion):
	def intermedio(request, *args, **kwarks):
		cuenta = DatosHost.objects.all().count()
		if cuenta == 0:
			return HttpResponseRedirect('/datos/conexion?next=/')
		else:
			return funcion(request)
	return intermedio

def crossite_redirection_decorator(funcion):
	def intermedio(request, *args, **kwarks):
		try:
			request.META['HTTP_REFERER']
		except KeyError:
			return HttpResponseRedirect('/')
		else:
			return funcion(request)
	return intermedio