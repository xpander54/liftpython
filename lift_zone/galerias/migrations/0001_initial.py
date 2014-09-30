# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Galeria'
        db.create_table(u'galerias_galeria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'galerias', ['Galeria'])

        # Adding model 'Imagen'
        db.create_table(u'galerias_imagen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('galeria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['galerias.Galeria'])),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'galerias', ['Imagen'])


    def backwards(self, orm):
        # Deleting model 'Galeria'
        db.delete_table(u'galerias_galeria')

        # Deleting model 'Imagen'
        db.delete_table(u'galerias_imagen')


    models = {
        u'galerias.galeria': {
            'Meta': {'object_name': 'Galeria'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'galerias.imagen': {
            'Meta': {'object_name': 'Imagen'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'galeria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['galerias.Galeria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['galerias']