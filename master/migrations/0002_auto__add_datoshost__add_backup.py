# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DatosHost'
        db.create_table(u'master_datoshost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('host', self.gf('django.db.models.fields.CharField')(default='localhost', max_length=50)),
            ('usuario', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'master', ['DatosHost'])

        # Adding model 'Backup'
        db.create_table(u'master_backup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base_nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'master', ['Backup'])


    def backwards(self, orm):
        # Deleting model 'DatosHost'
        db.delete_table(u'master_datoshost')

        # Deleting model 'Backup'
        db.delete_table(u'master_backup')


    models = {
        u'master.backup': {
            'Meta': {'object_name': 'Backup'},
            'base_nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'master.datoshost': {
            'Meta': {'object_name': 'DatosHost'},
            'host': ('django.db.models.fields.CharField', [], {'default': "'localhost'", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'usuario': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['master']