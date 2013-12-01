# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IpServer'
        db.create_table(u'master_ipserver', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('hora_y_fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'master', ['IpServer'])


    def backwards(self, orm):
        # Deleting model 'IpServer'
        db.delete_table(u'master_ipserver')


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
        },
        u'master.ipserver': {
            'Meta': {'object_name': 'IpServer'},
            'hora_y_fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'})
        }
    }

    complete_apps = ['master']