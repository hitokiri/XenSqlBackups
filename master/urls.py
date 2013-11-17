from django.conf.urls import url, patterns

urlpatterns = patterns('master.views',
	url(r'^$', 'vista_index', name = 'index'),
	url(r'^login/$', 'vista_login', name = 'login'),
	)