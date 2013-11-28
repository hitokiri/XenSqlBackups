#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from master.forms import LoginForm, SalvadoForm, DatosForm
from master.decorators import datos_decorator, crossite_redirection_decorator
from master.models import DatosHost, Backup
import shlex
import subprocess
import os


def vista_index(request):
	args = shlex.split("service mysql status")
	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	dump_output, error = p.communicate()
	instalado = error
	estado = dump_output.split('/')[0].split(' ')[1]
	datoshost = DatosHost.objects.all().count()
	backup = Backup.objects.all().count()
	ctx = {'instalado': instalado, 'estado': estado, 'datoshost': datoshost, 'backup': backup}
	return render_to_response('index.html', ctx, context_instance = RequestContext(request))

@login_required(login_url = '/login')
@datos_decorator
@crossite_redirection_decorator
def vista_crear_conexion(request):
	error_datos = ""
	cnf = '/home/hiko/Escritorio/archivo.cnf'
	filepath = '/home/hiko/Escritorio/salida.txt'
	no_backup = ['Database', 'information_schema', 'performance_schema', 'test', 'mysql']
	args = shlex.split("mysql --defaults-extra-file=%s --execute='show databases'" % cnf)
	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	dump_output, error_datos = p.communicate()
	lista_db = dump_output.strip().split('\n')
	for item in no_backup:
	      lista_db.remove(item)
	if request.method == 'POST':
		formulario = SalvadoForm(request.POST)
		if formulario.is_valid():
			dato = formulario.save(commit =False)
			print dato.base_nombre
			return  HttpResponseRedirect('/')
	else:
		formulario = SalvadoForm()
	ctx = {'lista_db' : lista_db, 'formulario': formulario}
	return render_to_response('backups.html', ctx, context_instance = RequestContext(request))

@login_required(login_url = '/login')
@crossite_redirection_decorator
def vista_listar_buscar(request):
	return render_to_response('mostrar_buscar.html',context_instance = RequestContext(request))


@login_required(login_url = '/login')
@crossite_redirection_decorator
def vista_logout(request):
	try:
		logout_salir = request.META['HTTP_REFERER'].split('http://'+request.META['HTTP_HOST'])[1][:-1]
		logout(request)
		return HttpResponseRedirect('/login')

	except KeyError:
		return HttpResponseRedirect('/')

def vista_login(request):
	try:
		meta = request.META['QUERY_STRING'].split('=')[1]
	except IndexError:
		meta = None
	error 	= ''
	vista 	= 'Login'
	if request.method == 'POST':
		formulario = LoginForm(request.POST)
		if formulario.is_valid():
			usuario 	= formulario.cleaned_data['usuario']
			password 	= formulario.cleaned_data['password']
			user 		=  authenticate(username = usuario, password = password)
			if user:
				if user.is_active:
					login(request, user)
					if meta:
						return HttpResponseRedirect(meta)
					else:
						return HttpResponseRedirect('/login')
			else:
				error='El usuario o la contraseña son erroneos, Por favor ingrese los datos correctamente'
	else:
		direccion = os.path.dirname(os.path.dirname(__file__))
		formulario = LoginForm()
		print meta
	ctx = {'formulario': formulario, 'error': error, 'vista': vista}
	return render_to_response('login.html',ctx, context_instance = RequestContext(request))

@login_required(login_url = '/login')
@crossite_redirection_decorator
def vista_datos_de_conexion(request):
	try:
		meta = request.META['QUERY_STRING'].split('=')[1]
	except IndexError:
		meta = None
	error= ''
	if request.method == 'POST':
		formulario = DatosForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			if meta:
				return HttpResponseRedirect(meta)
			else:
				return HttpResponseRedirect('/')
		else:
			error = 'Los datos ingresados no son correctos'
	else:
		formulario = DatosForm()
	ctx = {'formulario': formulario, 'error': error}

	return render_to_response('datos.html', ctx, context_instance = RequestContext(request))