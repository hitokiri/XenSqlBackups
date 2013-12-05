# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Backup.direccion'
        db.delete_column(u'master_backup', 'direccion')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Backup.direccion'
        raise RuntimeError("Cannot reverse this migration. 'Backup.direccion' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Backup.direccion'
        db.add_column(u'master_backup', 'direccion',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)


    models = {
        u'master.backup': {
            'Meta': {'object_name': 'Backup'},
            'base_nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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