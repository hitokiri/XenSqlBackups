from django.conf.urls import url, patterns

urlpatterns = patterns('master.views',
	url(r'^$', 'vista_index', name = 'index'),
	url(r'^login/$', 'vista_login', name = 'login'),
	url(r'^datos/conexion', 'vista_datos_de_conexion', name = 'conexion'),
	url(r'^logout/$', 'vista_logout', name = 'logout'),
	url(r'^backups/listado/$', 'vista_listar_backups', name = 'listar'),
	url(r'^backups/crear/$', 'vista_crear_backup', name = 'crear_backups'),
	)
