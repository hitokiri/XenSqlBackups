from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import shlex
import subprocess

def vista_index(request):
	cnf = '/home/hiko/Escritorio/archivo.cnf'
	filepath = '/home/hiko/Escritorio/salida.txt'
	no_backup = ['Database', 'information_schema', 'performance_schema', 'test', 'mysql']
	args = shlex.split("mysql --defaults-extra-file=%s --execute='show databases'" % cnf)

	p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	dump_output= p.communicate()[0]
	lista_db = dump_output.strip().split('\n')
	for item in no_backup:
	      lista_db.remove(item)
	ctx = {'lista_db' : lista_db}
	return render_to_response('index.html', ctx, context_instance = RequestContext(request))

def vista_login(request):
	return render_to_response('login.html', context_instance = RequestContext(request))