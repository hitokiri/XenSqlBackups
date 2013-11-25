#coding:utf-8
from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput
from master.models import Backup, DatosHost
import shlex, subprocess
class LoginForm(forms.Form):
	usuario 	= forms.CharField(max_length = 20)
	password 	= forms.CharField(max_length = 20, widget = PasswordInput(), label = u'Contraseña')

class SalvadoForm(forms.ModelForm):
	class Meta:
		model 	= Backup
		exclude = ('direccion',)

class DatosForm(forms.ModelForm):
	def clean(self):
		error = None
		cleaned_data = self.cleaned_data
		host = cleaned_data.get('host')
		usuario = cleaned_data.get('usuario')
		password = cleaned_data.get('password')
		args = shlex.split("mysql  --user=%s --host=%s --password=%s  --execute='show databases'" % (usuario,host,password))
		p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		error = p.communicate()[1]
		if error:
			raise forms.ValidationError('Los datos ingresados no son correctos')
		return cleaned_data

	class Meta:
		model 	= DatosHost

