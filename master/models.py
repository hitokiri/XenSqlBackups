#coding:utf-8
from django.db import models

# Create your models here.
class Backup(models.Model):
	base_nombre 			= models.CharField(max_length=50)
	direccion 				= models.CharField(max_length=50)
	fecha_creacion 			= models.DateField(auto_now_add = True)

class DatosHost(models.Model):
	host 					= models.CharField( max_length=50, default='localhost')
	usuario 				= models.CharField( max_length=50)
	password 				= models.CharField( max_length=50)
	class Meta:
		verbose_name 		= ('DatosHost')
		verbose_name_plural = ('DatosHosts')

