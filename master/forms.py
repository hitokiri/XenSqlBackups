#coding:utf-8
from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput , TextInput
from master.models import Backup, DatosHost, Restore
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
		fields = ('password','host', 'usuario')
		widgets = {
			'password': PasswordInput(attrs = {'class': 'form-control input-sm', 'placeholder':"Password", 'required':"required", 'title':"Debe ingresar un password valido"}),
			'usuario' : TextInput(attrs = {'class': 'form-control input-sm', 'placeholder': 'usuario', 'required':"required", 'title':"Debe ingresar un usuario valido"}),
			'host' : TextInput(attrs = {'class': 'form-control input-sm', 'placeholder': 'host', 'required':"required", 'title':"Debe ingresar un host valido"}),
		}

class RestoreForm(forms.ModelForm):
    class Meta:
        model = Restore
        exclude = ('nombre_archivo',)
