#coding:utf-8
from django import forms
from django.forms.widgets import PasswordInput


class FormLogin(forms.Form):
	usuario = forms.CharField(max_length = 20)
	password = forms.CharField(max_length = 20, widget = PasswordInput(), label=u'Contraseña')