#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from master.forms import LoginForm, SalvadoForm, DatosForm
from master.decorators import datos_decorator, crossite_redirection_decorator
from master.models import DatosHost, Backup
import shlex
import subprocess
import os
import datetime

def vista_index(request):
	args = shlex.split("service mysql status")
	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	dump_output, error = p.communicate()
	instalado = error
	estado = 'start' in dump_output
	datoshost = DatosHost.objects.all().count()
	backup = Backup.objects.all().count()
	ctx = {'instalado': instalado, 'estado': estado, 'datoshost': datoshost, 'backup': backup}
	return render_to_response('index.html', ctx, context_instance = RequestContext(request))

@login_required(login_url = '/login')
@datos_decorator
@crossite_redirection_decorator
def vista_crear_backup(request):
	datos_conexion = DatosHost.objects.get(pk=1)
	error_datos = ""
	direccion = os.path.join(settings.DIRECCION_BASE[0],'SqlBackup/')
	no_backup = ['Database', 'information_schema', 'performance_schema', 'test', 'mysql']
	args = "mysql  --user=%s --host=%s --password=%s  --execute='show databases'" % (datos_conexion.usuario,
						datos_conexion.host,datos_conexion.password)
	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	dump_output, error_datos = p.communicate()
	lista_db = dump_output.strip().split('\n')
	for item in no_backup:
	      lista_db.remove(item)
	if request.method == 'POST':
		formulario = SalvadoForm(request.POST)
		if formulario.is_valid():
			dato = formulario.save(commit =False)
			lista_db_request = map(str.strip, str(dato.base_nombre).split(','))
			for db in lista_db_request:
				if db in lista_db:
					generador_nombre_db = db + '-' +str(datetime.datetime.now().strftime('%m-%d-%Y-%I:%M:%S-%p-%Z')) + '.sql'
					args_dump = "mysqldump  --user=%s --host=%s --password=%s  %s > %s%s" % (datos_conexion.usuario,
											datos_conexion.host,datos_conexion.password, db, direccion, generador_nombre_db)
					proceso_backup = subprocess.Popen(args_dump, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
					dump_output_backup, error_datos_backup = proceso_backup.communicate()
					backups_manuales = Backup()
					backups_manuales.base_nombre = generador_nombre_db
					backups_manuales.save()

			return  HttpResponseRedirect('/')
	else:
		formulario = SalvadoForm()
	ctx = {'lista_db' : lista_db, 'formulario': formulario}
	return render_to_response('backups.html', ctx, context_instance = RequestContext(request))

@login_required(login_url = '/login')
@crossite_redirection_decorator
def vista_listar_backups(request):
	listar = Backup.objects.all()
	ctx = {'listar': listar}
	return render_to_response('mostrar_buscar.html', ctx, context_instance = RequestContext(request))


@login_required(login_url = '/login')
@crossite_redirection_decorator
def vista_logout(request):
	try:
		logout_salir = request.META['HTTP_REFERER'].split('http://'+request.META['HTTP_HOST'])[1][:-1]
		logout(request)
		return HttpResponseRedirect('/login')

	except KeyError:
		return HttpResponseRedirect('/')
@crossite_redirection_decorator
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

@login_required(login_url = '/login')
@crossite_redirection_decorator
def vista_editar_datos_de_conexion(request):
	try:
		meta = request.META['QUERY_STRING'].split('=')[1]
	except IndexError:
		meta = None
	error= ''
	consulta = DatosHost.objects.get(pk=1)

	if request.method == 'POST':
		formulario = DatosForm(request.POST, instance=consulta)
		if formulario.is_valid():
			print 'valido'
			formulario.save()
			if meta:
				return HttpResponseRedirect(meta)
			else:
				return HttpResponseRedirect('/')
		else:
			error = 'Los datos ingresados no son correctos'
	else:
		formulario = DatosForm(instance =consulta)
	ctx = {'formulario': formulario, 'error': error}
	return render_to_response('editar_datos.html', ctx, context_instance = RequestContext(request))