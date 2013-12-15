# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Backups'
        db.create_table(u'master_backups', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subido', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('backups_realizados', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('nombre_archivo', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'master', ['Backups'])


    def backwards(self, orm):
        # Deleting model 'Backups'
        db.delete_table(u'master_backups')


    models = {
        u'master.backup': {
            'Meta': {'object_name': 'Backup'},
            'base_nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'master.backups': {
            'Meta': {'object_name': 'Backups'},
            'backups_realizados': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_archivo': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'subido': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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