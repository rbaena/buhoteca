# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Libro'
        db.create_table(u'libros_libro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('editorial', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['autores.Autor'])),
        ))
        db.send_create_signal(u'libros', ['Libro'])


    def backwards(self, orm):
        # Deleting model 'Libro'
        db.delete_table(u'libros_libro')


    models = {
        u'autores.autor': {
            'Meta': {'object_name': 'Autor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nacionalidad': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'libros.libro': {
            'Meta': {'object_name': 'Libro'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['autores.Autor']"}),
            'editorial': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['libros']