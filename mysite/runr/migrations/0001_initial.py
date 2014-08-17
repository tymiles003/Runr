# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timer'
        db.create_table('runr_timer', (
            ('key', self.gf('django.db.models.fields.SlugField')(primary_key=True, max_length=50)),
            ('text', self.gf('django.db.models.fields.CharField')(blank=True, max_length=100)),
            ('creator', self.gf('django.db.models.fields.CharField')(blank=True, max_length=20)),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('runr', ['Timer'])


    def backwards(self, orm):
        # Deleting model 'Timer'
        db.delete_table('runr_timer')


    models = {
        'runr.timer': {
            'Meta': {'object_name': 'Timer'},
            'creator': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '20'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'key': ('django.db.models.fields.SlugField', [], {'primary_key': 'True', 'max_length': '50'}),
            'text': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['runr']