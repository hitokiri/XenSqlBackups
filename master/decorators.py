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

