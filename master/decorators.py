#coding:utf-8
from master.models import DatosHost
from django.http import HttpResponseRedirect
import subprocess

def datos_decorator(funcion):
	def intermedio(request, *args, **kwarks):
		cuenta = DatosHost.objects.all().count()
		datos_conexion = DatosHost.objects.get(pk=1)
		args = "mysql  --user=%s --host=%s --password=%s  --execute='show databases'" % (datos_conexion.usuario,
											datos_conexion.host,datos_conexion.password)
		proceso = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
		dump_output, error = proceso.communicate()
		if error:
			return HttpResponseRedirect('/datos/conexion/editar/')
		elif cuenta == 0:
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